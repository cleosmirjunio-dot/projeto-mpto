from github_report.src.github_client import GithubClient
from github_report.src.report_service import ReportService

    
def main():

    client = GithubClient()

    repos = client.get_repos("cleosmirjunio-dot")

    report = ReportService(repos)

    print("Relatório Geral")
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

    # Se quiser detalhes completos, deixe separado:
    print("\nDetalhes dos Repositórios")
    print("-" * 40)
    for repo in repos:
        print(repo)
        print("-" * 40)

       

if __name__ == "__main__":
    main()