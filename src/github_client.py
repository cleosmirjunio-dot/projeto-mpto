import requests
from src.reposito
class GithubClient:
    BASE_URL = "https://api.github.com/users"

    def get_repos(self, username: str) -> list[dict]:
        '''
        Busca os repositórios públicos de um usuário no GitHub
        Args:
            username (str) : Nome do usuário no GitHub

        Returns:
            lis[dict]: lista de repositórios em formato JSON

        raises:
            valueError: Se o usuário não existir ou limite for atingido.
            connectionError: Se houver falha de conexão
            TimeoutError: Se a requisição demorar demais.
        '''

        pass
