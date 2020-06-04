### Instalação Após Clonagem do Projeto.

1. Criar Ambiente Virtual. [Link tutorial](https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv/)

2. Após ativar o ambiente instalar as dependências do projeto a partir do comando:
```sh
pip install -r requirements.txt
```

3. Criar um container Docker do Postgres.
```sh
docker run --name farma-dashboard -e POSTGRES_PASSWORD=docker -p 5433:5432 -d -t postgres
```

4. Criar um banco de dados no servidor do postgres.

5. Conectar a aplicação ao banco de dados no arquivo settings.py

EX:
```python
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'farma-dashboard',
        'USER': 'postgres',
        'PASSWORD': 'docker',
        'HOST': '127.0.0.1',
        'PORT': '5433',
    }
```

6. Rodar os comandos: 

`python manage.py makemigrations` para criar os migrations

`python manage.py migrate` aplicar migrations no banco de dados

`python manage.py runserver` rodar servidor local na url: https://localhost:8000