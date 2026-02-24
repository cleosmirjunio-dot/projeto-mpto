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
        
        #=========Tratamento de erros =============
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                raise ValueError("Usuário não encontrado")
            elif response.status_code == 403:
                raise ValueError("Limit de requisições atingida")
            else:
                raise

        except requests.exceptions.ConnectionError:
            raise ConnectionError ("Falha na conexão com o servidor")

        except requests.exceptions.Timeout:
            raise TimeoutError ("A requisição demorou demais")

        data = response.json()# Pega o corpo da resposta HTTP e converte de JSON(texto), para objeto Pyton
        return [Repository.from_api(repo) for repo in data]
    


