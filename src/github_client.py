import requests
from github_report.src.repository import Repository

class GithubClient:
    BASE_URL = "https://api.github.com"

    def get_repos(self, username: str) -> list[Repository]:
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

        url = self.BASE_URL + f"/users/{username}/repos"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            if response.status_code == 404:
                raise ValueError("User not found")
            elif response.status_code == 403:
                raise ValueError("Limit de requisições atingida")
            else:
                raise

        except requests.exceptions.ConnectionError:
            raise ConnectionError ("Falha na conexão com o servidor")

        except requests.exceptions.Timeout:
            raise "A requisição demorou demais"

        data = response.json()
        return [Repository.from_api(repo) for repo in data]
    


