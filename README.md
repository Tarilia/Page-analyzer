[![Actions Status](https://github.com/Tarilia/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Tarilia/python-project-83/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/4e6d0665b9c3bf7f4540/maintainability)](https://codeclimate.com/github/Tarilia/python-project-83/maintainability)

### Page analyzer:
Демо-версию сайта можно посмотреть [здесь](https://page-analyzer-pv9i.onrender.com).
Проект создан для проверки сайтов на [SEO](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F)
пригодность, анализирует HTML-теги и отображает информацию в таблице для каждого сайта.

### Визуализация:
[![viber-2023-12-04-20-12-03-467.jpg](https://i.postimg.cc/dQ4QBSnb/viber-2023-12-04-20-12-03-467.jpg)](https://postimg.cc/dDZKQ6b6)

[![viber-2023-12-04-20-01-00-019.jpg](https://i.postimg.cc/jdWyzNtr/viber-2023-12-04-20-01-00-019.jpg)](https://postimg.cc/hfBJnXXC)

[![2024-05-22-144405.png](https://i.postimg.cc/9X62szjn/2024-05-22-144405.png)](https://postimg.cc/V5W2Cfvq)

### Установка:
```
$ скачайте проект
$ cd python-project-83  
$ make install
$ make dev - запустить сервер в среде разработчика
  Создайте файл «.env» в корневой папке и добавьте в него следующие переменные: 
    - SECRET_KEY={secret_key}  
    - DATABASE_URL={provider}://{user}:{password}@{host}:{port}/{db}  
    - REDIS_URL=redis://{host}:{port}

```
### Docker:
```
$ скачайте проект
$ cd python-project-83
  Создайте файл «.env» в корневой папке и добавьте в него следующие переменные:
    - SECRET_KEY={secret_key}
    - POSTGRES_PASSWORD
    - POSTGRES_USER
    - POSTGRES_DB
    - DATABASE_URL={provider}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{host}:{port}/{POSTGRES_DB}
    - REDIS_URL=redis://{host}:{port}
    - docker-compose up

```

### Библиотеки:
 - [python "^3.10"](https://www.python.org/)
 - [poetry](https://python-poetry.org/)
 - [flask](https://flask.palletsprojects.com/en/3.0.x/)
 - [gunicorn](https://docs.gunicorn.org/en/stable/)
 - [python-dotenv](https://github.com/theskumar/python-dotenv)
 - [psycopg2](https://www.psycopg.org/)
 - [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 - [postgresql](https://www.postgresql.org/)
 - [requests](https://requests.readthedocs.io/en/latest/)
 - [validators](https://python-validators.github.io/validators/)
 - [flake8](https://flake8.pycqa.org/)

