import json
import csv
from pathlib import Path

class FileStorage:
    ''' Responsável por salvar dados em arquivos JSON e CSV'''

    def __init__(self, base_path = "data"):
        """
        Inicializa o armazenamento definindo a pasta base.

        Args:
            base_path (str): Pasta onde os arquivos serão salvos.
        """
        try:
            self.base_path = Path(base_path)
            self.base_path.mkdir(exist_ok=True)
        except PermissionError:
            raise PermissionError(
                "Sem permisão para acessar ou criar o diretório informado"
                "\nOs Arquivos não foram gerados"
            ) 

    def save_json(self, filename: str, data:list[dict]) -> str:
        """
        Salva uma lista de dicionários em formato JSON.

        Args:
            filename (str): Nome do arquivo (sem extensão).
            data (list[dict]): Dados a serem salvos.
        """  
        file_path = self.base_path / f"{filename}.json"

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        return str(file_path)    
                
    def save_csv(self, filename: str, data: list[dict]) -> None:
        """
        Salva uma lista de dicionários em formato CSV.

        Args:
            filename (str): Nome do arquivo (sem extensão).
            data (list[dict]): Dados a serem salvos.
        """
        if not data:
            return
        
        file_path = self.base_path / f"{filename}.csv"

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()#Escreve o cabeçalho do arquvo 
            writer.writerows(data)
        
        return(file_path)    
