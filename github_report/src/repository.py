class Repository:
    """
    Representa um repositório do GitHub dentro do domínio da aplicação.

    Esta classe atua como uma entidade, modelando os principais
    atributos de um repositório retornado pela API do GitHub.

    A entidade encapsula os dados do repositório e pode conter
    comportamentos e regras relacionadas ao domínio.
    """
    def __init__(self,
                 id:str,
                 name: str,
                 full_name: str,
                 html_url: str,
                 language: str | None,
                 stargazers_count: int,
                 forks_count: int,
                 updated_at: str,
                 open_issues_count: int,
                 ):
        self.id = id
        self.name = name
        self.full_name = full_name
        self.html_url = html_url
        self.language = language
        self.stargazers_count = stargazers_count
        self.forks_count = forks_count
        self.updated_at = updated_at
        self.open_issues_count = open_issues_count

    def __str__(self):
        return(
            f"Id: {self.id}\n"
            f"Nome: {self.name}\n"
            f"Nome completo: {self.full_name}\n"
            f"URL: {self.html_url}\n"
            f"Linguagem principal: {self.language}\n"
            f"Estrelas: {self.stargazers_count}\n"
            f"Forks: {self.forks_count}\n"
            f"Última atualizado em: {self.updated_at}\n" 
            f"Problemas não resolvidos: {self.open_issues_count}"
        )

    @classmethod
    def from_api(cls, data: dict) -> "Repository":
        """
    Cria uma instância de Repository a partir
    de um dicionário retornado pela API do GitHub.

    Args:
        data (dict): Dicionário contendo os dados
                     de um repositório retornado pela API.

    Returns:
        Repository: Objeto Repository com os dados mapeados
                    para os atributos da entidade.

    Observação:
        Este método atua como um Factory Method,
        convertendo dados brutos (JSON/dict) em
        uma entidade estruturada do domínio.
    """
        return cls(

            id=data.get("id"),
            name=data.get("name"),
            full_name=data.get("full_name"),
            html_url=data.get("html_url"),
            language=data.get("language"),
            stargazers_count=data.get("stargazers_count"),
            forks_count=data.get("forks_count"),
            updated_at=data.get("updated_at"),
            open_issues_count=data.get("open_issues_count")
        )
    def __repr__(self) -> str:
        """Retorna uma representação simples do repositório para debug."""
        return f"<repository name={self.full_name} >"
    
    def to_dict(self) -> dict:
        """Converte o repositório em dicionário para salvar em JSON ou CSV."""
        return {
            "name": self.name,
            "stargazers_count": self.stargazers_count,
            "language": self.language,
            "html_url": self.html_url,
        }