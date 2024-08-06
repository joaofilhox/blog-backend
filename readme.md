## Backend

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em seu ambiente de desenvolvimento:

- **Python 3.12.3**: [Instalar Python](https://www.python.org/downloads/release/python-3123/)
- **PostgreSQL**: [Instalar PostgreSQL](https://www.postgresql.org/download/)
- **pip** (gerenciador de pacotes do Python): Geralmente vem com o Python
- **virtualenv** (opcional, mas recomendado): [Tutorial virtualenv](https://youtu.be/hA2l0TgaZhM?si=uisvvaKOCNMeQ_j9)
- **Git**: [Instalar Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Configuração do Ambiente

Siga as etapas abaixo para configurar e rodar o projeto localmente.

### 1. Clonar o Repositório

Primeiro, clone o repositório do projeto para a sua máquina local.
```sh
git clone https://github.com/Hanami-Staff/SQUAD-21.git
cd SQUAD-21
```
### 2. Criar e Ativar um Ambiente Virtual
Recomendo usar um ambiente virtual para gerenciar as dependências do projeto e evitar conflitos com outras bibliotecas do Python instaladas no seu sistema.

#### como faço isso:
##### No Linux/MacOS
```sh 
python3 -m venv venv
source venv/bin/activate
```
##### No Windows
```sh 
python -m venv venv
venv\Scripts\activate
```
### 3. Instalar as Dependências
Com o ambiente virtual ativado, instale todas as dependências necessárias executando:
```sh 
pip install -r requirements.txt
```
### 4. Configurar as Variáveis de Ambiente
#### 1. Copie o arquivo de exemplo .env.example e renomeie para .env. Este arquivo será usado para armazenar suas configurações específicas do ambiente local.
```sh
cp .env.example .env
```
#### 2. Abra o arquivo .env em um editor de texto e preencha as variáveis com os valores apropriados. Aqui está um exemplo com algumas variáveis preenchidas:
```env
SECRET_KEY='seu_valor_secreto_aqui'
POSTGRES_USER='seu_usuario'
POSTGRES_PASSWORD='sua_senha'
POSTGRES_DBNAME='nome_do_banco'
POSTGRES_HOST='localhost'
POSTGRES_PORT=5432
```
Substitua seu_valor_secreto_aqui, seu_usuario, sua_senha, nome_do_banco, localhost e 5432 pelos valores corretos para o seu ambiente.

### 5. Instruções para Rodar a API
#### 1. Criar e Aplicar Migrações do Banco de Dados
Antes de iniciar o servidor pela primeira vez, é importante criar e aplicar as migrações para garantir que o banco de dados esteja atualizado com as últimas alterações de modelo. Para fazer isso, execute os seguintes comandos na sequência:

```sh
python manage.py makemigrations
python manage.py migrate
```
#### 2.Executar o Servidor de Desenvolvimento
Agora você pode iniciar o servidor de desenvolvimento do Django:
```sh
python manage.py runserver
```
O servidor estará disponível em http://127.0.0.1:8000/.

## Acessar a Documentação da API
Teste para ver a documentação da API disponível através do Swagger. Você pode acessar a seguinte URL:
- **Interface Swagger**: http://127.0.0.1:8000/api/docs/swagger/
