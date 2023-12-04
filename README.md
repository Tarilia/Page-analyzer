[![Actions Status](https://github.com/Tarilia/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Tarilia/python-project-83/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/4e6d0665b9c3bf7f4540/maintainability)](https://codeclimate.com/github/Tarilia/python-project-83/maintainability)

### Page analyzer app:
A demo version of the site can be viewed [here](https://page-analyzer-pv9i.onrender.com).
The project was created to check sites for [SEO](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F)
suitability, analyzes HTML tags and displays information in a table for each site.

### Visualization:
[![viber-2023-12-04-20-12-03-467.jpg](https://i.postimg.cc/dQ4QBSnb/viber-2023-12-04-20-12-03-467.jpg)](https://postimg.cc/dDZKQ6b6)

[![viber-2023-12-04-20-01-00-019.jpg](https://i.postimg.cc/jdWyzNtr/viber-2023-12-04-20-01-00-019.jpg)](https://postimg.cc/hfBJnXXC)

[![viber-2023-12-04-20-01-00-041.jpg](https://i.postimg.cc/jq3zwvVX/viber-2023-12-04-20-01-00-041.jpg)](https://postimg.cc/4ntKj6x7)

### Installing and launching the application:
```
$ download the project
$ cd python-project-83  
$ make install
$ make dev - start server in developer enironment
  Create a ".env" file in the root folder and add the following variables to it: 
    - SECRET_KEY={secret_key}  
    - DATABASE_URL={provider}://{user}:{password}@{host}:{port}/{db}  
$ make start - start production gunicorn server
```
### Languages and Tools:
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

