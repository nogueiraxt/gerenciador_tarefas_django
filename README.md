#  Gerenciador de Tarefas com Django

![Python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-4.2-092E20.svg?style=for-the-badge&logo=django)

Este projeto é uma aplicação web simples para gerenciamento de tarefas, desenvolvida com Python e o framework Django. Ele permite que o usuário adicione, visualize, edite e remova tarefas de forma organizada e persistente.

O projeto foi criado como uma migração de uma aplicação desktop feita em Tkinter para uma solução web moderna e acessível por navegador.

## ✨ Funcionalidades

- **Adicionar Tarefas:** Crie novas tarefas com descrição, data de início, data de término e status.
- **Listar Tarefas:** Visualize todas as tarefas cadastradas em uma tabela organizada.
- **Editar Tarefas:** Modifique os detalhes de qualquer tarefa existente.
- **Remover Tarefas:** Exclua tarefas individualmente.
- **Limpeza Rápida:** Remova todas as tarefas já concluídas com um único clique.
- **Painel de Administração:** Gerencie todas as tarefas através da interface de administrador nativa do Django.

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python
- **Framework:** Django
- **Banco de Dados:** SQLite3 (padrão do Django para desenvolvimento)
- **Frontend:** HTML5, CSS3

## 🚀 Como Rodar o Projeto Localmente

Siga os passos abaixo para executar o projeto em sua máquina.

### **Pré-requisitos**

- [Python 3.9+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### **Instalação**

1.  **Clone o repositório:**
    ```bash
    git clone URL_DO_SEU_REPOSITORIO_AQUI
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd gerenciador_tarefas_django
    ```

3.  **(Recomendado) Crie e ative um ambiente virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install Django
    ```

### **Configuração do Banco de Dados**

1.  Com o ambiente virtual ativado e dentro da pasta do projeto, execute os comandos abaixo para criar o banco de dados e as tabelas:
    ```bash
    # Cria os arquivos de migração
    python manage.py makemigrations tarefas

    # Aplica as migrações, criando o banco de dados
    python manage.py migrate
    ```

### **Execução**

1.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

2.  Abra seu navegador e acesse: `http://127.0.0.1:8000/`

### **(Opcional) Criando um Superusuário**

Para acessar o painel de administração (`/admin`), você precisa criar um superusuário.

1.  Execute o comando:
    ```bash
    python manage.py createsuperuser
    ```
2.  Siga as instruções para criar um nome de usuário, e-mail e senha.
3.  Acesse o painel de admin em: `http://127.0.0.1:8000/admin/`

## 👨‍💻 Autor

- **Nogueira Pinheiro** - https://github.com/nogueiraxt
