# Pele & Osso Gym

Uma aplicação de gerenciamento de academia feito como avaliação da disciplina de Desenvolvimento WEB II do curso de Licenciatura em Informática do IFPI - Campus Teresina Zona Sul

## Bibliotecas utilizadas

- Flask
- Flask-WTF
- Flask-SQLAlchemy
- WTForms-SQLAlchemy
- Flask-Login
- validate-docbr

## Requisitos

- Python 3.6
- Pipenv

## Como começar

Clone este repositório e ente na pasta do projeto

```sh
git clone https://github.com/CleysonPH/pele_osso_gym.git
cd pele_osso_gym
```

Instale os requisitos do projeto com o pipenv

```sh
pipenv install
```

## Como rodar esse projeto

Inicie o ambiente virtual

```sh
pipenv shell
```

Depois crie o banco de dados

```sh
python

>>> form model import db
>>> db.create_all()
```

E por ultimo basta executar o servidor de desenvolvimento do Flask

```sh
flask run
```

E então acessar a aplicação em http://localhost:5000/
