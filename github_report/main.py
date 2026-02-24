import argparse
from datetime import datetime
from github_report.src.github_client import GithubClient
from github_report.src.report_service import ReportService
from github_report.src.file_storage import FileStorage


def generate_timestamp() -> str:
    '''Define data  e hora no nome do arquivo '''
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def parse_args():
    '''Configura e processa os argumentos da linha de comando.
       A aplicação exige dois parâmetros obrigatórios:
       --username: nome do usuário no GitHub
       --out : diretório onde os arquivos gerados serão salvos

       Returns
            argparse.Namespace: objeto contendo os argumentosinformados
            pelo usuário na execuçao do programa. 
    '''
    parser = argparse.ArgumentParser(
        description="Coletor de Dados da API do GitHub"
    )

    parser.add_argument(
        "--username",
        required=True,
        help="Usuário do GitHub"

    )
    
    parser.add_argument(
        "--out",
        required=True,
        help="Diretório de saída"
    )

    return parser.parse_args()
    
def main():
    args = parse_args()
    username = args.username
    output_dir = args.out
        
    client = GithubClient()

    try:
        repos = client.get_repos(username)
    except Exception as e:
        print(f"\nErro: {e}")    
        return

    if not repos:
        print("\nUsuário não possui repositórios públicos.")
        return

    report = ReportService(repos)

    
 # ===== Exibe o relatório no terminal =====
    

    print(f"Relatório dos repositórios de {username}")
    print("_" * 40)

    #Totais
    print("Total de repositórios:", report.total_repositories())
    print("Total de estrelas:", report.total_stars())
    
    # Top 5
    print("\nTop 5 por Estrelas")
    for repo in report.top_5_by_stars():
        print(f"{repo.name} - {repo.stargazers_count}")

    # Linguagens
    print("\nRepositórios por linguagem:")
    for lang, total in report.count_by_language().items():
        print(f"{lang}: {total}")

    # detalhes dos repositórios:
    print("\nDetalhes dos Repositórios")
    print("-" * 40)

    for repo in repos:
        print(repo)
        print("-" * 40)

    timestamp = generate_timestamp()    

    
    repos_dict = [repo.to_dict() for repo in repos]
    try:
        storage = FileStorage(base_path=output_dir)
    except PermissionError as e:
        print(f"Erro: {e}")
        return

    json_file = storage.save_json( f"repos_{username}_{timestamp}", repos_dict)

    report_sumary = report.generate_summary()
    csv_file = storage.save_csv(
        f"report_{username}_{timestamp}", report_sumary
    )


    print("\nForam gerados os seguintes arquivos: ")
    print(f"- {json_file}")
    print(f"- {csv_file}")
    
       

if __name__ == "__main__":
    main()


   #Exemplo para rodar o codigo:    python3 -m github_report.main --username torvalds --out ./output