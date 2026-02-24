# 📊 GitHub Report

Projeto em Python para gerar relatórios de repositórios públicos de um usuário do GitHub.

## 🚀 Objetivo

Consumir a API pública do GitHub e gerar um relatório estruturado com informações dos repositórios de um usuário.

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Requests
- Programação Orientada a Objetos (POO)
- API REST (GitHub)

---

## 📂 Estrutura do Projeto


projeto-mpto/
│
├── github_report/
│ ├── main.py
│ └── src/
│ ├── github_client.py
│ ├── report_service.py
│ ├── file_storage.py
│ └── repository.py
│
├── requirements.txt
└── README.md


---

## ⚙️ Como executar

### 1️⃣ Clonar o repositório


git clone https://github.com/cleosmirjunio-dot/projeto-mpto.git

cd projeto-mpto


### 2️⃣ Criar ambiente virtual


python3 -m venv venv
source venv/bin/activate


### 3️⃣ Instalar dependências


pip install -r requirements.txt


### 4️⃣ Executar o projeto


python3 -m github_report.main --username torvalds --out ./output


---

## 📥 Parâmetros de Linha de Comando

O projeto utiliza argumentos via terminal para definir o usuário do GitHub e o diretório de saída do relatório.

### 🔹 Argumentos obrigatórios

| Argumento     | Tipo   | Descrição                                      | Exemplo     |
|---------------|--------|-----------------------------------------------|--------------|
| `--username`  | string | Nome do usuário no GitHub                    | torvalds      |
| `--out`       | string | Caminho da pasta onde o relatório será salvo | ./output      |


---

## 📌 Exemplo


python3 -m github_report.main --username torvalds --out ./output


---

## 📄 Resultado

O projeto gera um relatório estruturado com os dados dos repositórios retornados pela API do GitHub.

---

## 👨‍💻 Autor

Cleosmir Junio
