import requests
from datetime import date

from page_analyzer.celery_config import celery_app
from page_analyzer.database import get_all_urls, add_checks_url
from page_analyzer.parser import parse_response

@celery_app.task
def check_all_urls():
    urls = get_all_urls()
    for url in urls:
        print(url['name'])
        try:
            response = requests.get(url['name'])
            status_code = response.status_code
        except requests.RequestException:
            add_checks_url(url['id'], 0, '', '',
                                   'Ошибка сети', date.today())
            print('Ошибка сети')
            continue
        h1, title, description = parse_response(response)
        add_checks_url(url['id'], status_code, h1, title,
                      description, date.today())
