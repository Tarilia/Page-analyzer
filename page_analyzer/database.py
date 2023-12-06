import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


def database_connection(func):
    def wrapper(*args, **kwargs):
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        connection = func(cur, *args, **kwargs)
        conn.commit()
        conn.close()
        return connection
    return wrapper


@database_connection
def get_url_name(cur, url):
    cur.execute("SELECT * FROM urls WHERE name=%s", (url, ))
    url_name = cur.fetchone()
    return url_name


@database_connection
def add_url(cur, url, created_at):
    cur.execute("INSERT INTO urls (name, created_at) VALUES (%s, %s) \
                RETURNING id", (url, created_at))
    url_data = cur.fetchone()
    return url_data


@database_connection
def get_url_id(cur, id):
    cur.execute("SELECT * FROM urls WHERE id=%s", (id, ))
    url_data = cur.fetchone()
    return url_data


@database_connection
def get_all_urls(cur):
    cur.execute("SELECT id, name FROM urls ORDER BY id DESC")
    data = cur.fetchall()
    return data


@database_connection
def get_all_check(cur, url_id):
    cur.execute("SELECT status_code, created_at FROM url_checks \
                WHERE url_id = (%s) ORDER BY id DESC", (url_id,))
    data = cur.fetchone()
    return data


@database_connection
def add_checks_url(cur, id, status_code, h1, title,
                   description, checked_date):
    url_id = get_url_id(id)['id']
    cur.execute("INSERT INTO url_checks (url_id, status_code, h1, title, \
                description, created_at) \
                VALUES (%s, %s, %s, %s, %s, %s) \
                RETURNING id, status_code, created_at",
                (url_id, status_code, h1, title,
                 description, checked_date))


@database_connection
def get_checks_url(cur, url_id):
    cur.execute("SELECT * FROM url_checks WHERE url_id=%s \
                ORDER BY id DESC", (url_id, ))
    checks = cur.fetchall()
    return checks
