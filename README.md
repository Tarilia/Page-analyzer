[![Actions Status](https://github.com/Tarilia/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Tarilia/python-project-83/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/4e6d0665b9c3bf7f4540/maintainability)](https://codeclimate.com/github/Tarilia/python-project-83/maintainability)

### Page analyzer app:
A demo version of the site can be viewed [here](https://page-analyzer-pv9i.onrender.com)
The project was created to check sites for [SEO](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F)
suitability, analyzes HTML tags and displays information in a table for each site.

### Installing and launching the application:
```
$ git clone git@github.com:Tarilia/python-project-83.git
$ cd python-project-83  
$ make install
$ make dev - start server in developer enironment
  Create a ".env" file in the root folder and add the following variables to it: 
    - SECRET_KEY={secret_key}  
    - DATABASE_URL={provider}://{user}:{password}@{host}:{port}/{db}  
$ make start - start production gunicorn server
```
### Languages and Tools:
 - Python "^3.10"
 - Pip
 - Poetry
 - Flask
 - Gunicorn
 - Python-dotenv
 - Psycopg2-binary
 - Pytest-cov
 - Beautifulsoup4
 - Postgresql
