from collections import Counter #Classe que conta ocorrências 
from github_report.src.repository import Repository

class ReportService():
    """
    Serviço responsável por gerar relatórios
    a partir de uma lista de Repository.
    """    
    
    def __init__(self, repositories:list[Repository]):
        self.repositories = repositories

    def __str__(self) -> str:
        lines = [
            f"Total de repositórios: {self.total_repositories()}",
            f"Total de estrelas: {self.total_stars()}",
            "\nRepositorios por linguagem:"
       ]

        for lang, total in self.count_by_language().items():
            lines.append(f"{lang}: {total}")

        return "\n".join(lines)

    # ====== Métricas Básicas =========
    

    def total_repositories(self) -> int:
        '''Retorna o total de repositórios'''
        return len(self.repositories)
    
    def total_stars(self) -> int:
        '''Retorna a soma total de estrelas'''
        return sum(repo.stargazers_count for repo in self.repositories)

    # ======= Top 5 estrelas ===========   


    def top_5_by_stars(self) -> list[Repository]:
        """
        Retorna os 5 repositórios com mais estrelas 
            return
                sorted() cria uma lista ordenada
        """
        return sorted(
            self.repositories,
            key=lambda repo: repo.stargazers_count,
            reverse=True #ordena do maior para o menor 
        )[:5]#pega apenas os 5 primeiros
    
    # ======== Contagem por linguagem ============

    def count_by_language(self) -> dict[str, int]:
        """
        Retorna um dicionário com a contagem de repositórios 
        por linguagem
        """
        languages = [
            repo.language or "Desconhecida"
            for repo in self.repositories
        ]
        return dict(Counter(languages))
    
    #======= Resumo para exportação CSV ============

    def generate_summary(self) -> list[dict]:
        '''
        Gera um resumo do relatório para 
        exportação em CSV.

        Returns:
            list[dict]: lista contendo metricas e valores.
                    
        '''
        sumary = [
            {"metric": "total_repositories", "value": self.total_repositories()},
            {"metric": "total_stars", "value": self.total_stars()},
            
        ]
        for lang, total in self.count_by_language().items():
            sumary.append(
                {"metric": f"language_{lang}", "value": total}
            )
        return sumary    