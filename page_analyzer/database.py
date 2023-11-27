import os
import psycopg2
from psycopg2.extras import DictCursor
from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


def database_connection(func):
    def wrapper(*args, **kwargs):
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor(cursor_factory=DictCursor)
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
    cur.execute("SELECT * FROM urls WHERE id=%s", (id,))
    url_data = cur.fetchone()
    return url_data


@database_connection
def get_all_urls(cur):
    cur.execute("SELECT * FROM urls ORDER BY id DESC")
    urls = cur.fetchall()
    return urls


@database_connection
def add_checks_url(cur, url_id, created_at_check):
    cur.execute("INSERT INTO url_checks (url_id, created_at) VALUES (%s, %s) \
                RETURNING id, created_at_check", (url_id, created_at_check))
    return None


@database_connection
def get_checks_url(cur, id):
    cur.execute("SELECT * FROM url_checks WHERE id=%s \
                ORDER BY id DESC", (id,))
    checks = cur.fetchall()
    return checks
