# FlaskProj

## 1. Contexto

O projeto FlaskProj é uma aplicação web desenvolvida utilizando Flask, um projeto desenvolvido para gerenciar um sistema de funcionários. Utilizando o framework Flask para o backend, este projeto permite criar, visualizar, atualizar e deletar registros de funcionários. Cada funcionário possui um CPF, nome e cargo. O projeto demonstra a utilização de um banco de dados SQLite juntamente com o SQLAlchemy para gerenciar os dados, e inclui várias páginas HTML estilizadas para uma interface de usuário amigável e intuitiva.

## 2. Configuração

Para configurar o projeto em sua máquina, siga os seguintes passos:

### Pré-requisitos

- Python 3.8 ou superior
- Virtualenv

### Passos de Configuração

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/leopxz/FlaskProj.git
   cd FlaskProj

2. Crie um ambiente virtual:
    ```bash
   python -m venv .venv
   
4. Ative o ambiente virtual:
No terminal bash, ou do vs code

No Windows:

    .venv\Scripts\activate

No Linux/Mac:
   
    source .venv/bin/activate

4. Instale as dependências:
     ```bash
   pip install -r requirements.txt


### Configuração do Banco de Dados

Inicialize o banco de dados:

    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade


### Execução

Para executar o projeto, siga os seguintes passos:
1. Ative o ambiente virtual, se ainda não estiver ativo:

No Windows:

    .venv\Scripts\activate

No Linux/Mac:

    source .venv/bin/activate

2. Execute a aplicação:

       python app.py

3. Acesse a aplicação:
Abra o navegador e vá para http://127.0.0.1:5000

### Estrutura
A estrutura do projeto é a seguinte:

FlaskProj/
│
├── controllers/
│   └── employeeController.py  # Controlador responsável pelas rotas e lógica de negócio
│
├── models/
│   └── employeeModel.py       # Modelo do banco de dados para os empregados
│
├── static/
│   └── css/
│       └── styles.css         # Arquivo CSS para estilização das páginas HTML
│
├── views/
│   ├── createpage.html        # Página para criar um novo empregado
│   ├── datalist.html          # Página para listar todos os empregados
│   ├── delete.html            # Página para confirmar a exclusão de um empregado
│   ├── mainpage.html          # Página principal
│   └── update.html            # Página para atualizar informações de um empregado
│
├── .gitignore                 # Arquivos e diretórios a serem ignorados pelo Git
├── LICENSE                    # Licença do projeto
├── README.md                  # Documentação do projeto
├── app.py                     # Arquivo principal da aplicação Flask
├── banco                      # Banco de dados SQLite
├── bancodedados.py            # Script para inicializar o banco de dados
└── requirements.txt           # Lista de dependências do projeto

