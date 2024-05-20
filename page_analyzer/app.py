from flask import (Flask, render_template, request, flash, redirect, url_for)
import os
from datetime import date
from dotenv import load_dotenv
from page_analyzer.url_processing import (validate_url, normalize_url)
from page_analyzer.parser import parse_response
from page_analyzer.database import (get_url_name, add_url, get_url_id,
                                    get_all_urls, add_checks_url,
                                    get_checks_url, get_all_check)
from page_analyzer.tasks import check_all_urls
import requests


load_dotenv()
app = Flask(__name__)


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def get_page():
    return render_template('index.html')


@app.post('/urls')
def post_urls():
    input_url = request.form.get('url')
    if not input_url:
        flash('URL обязателен', 'danger')
        return render_template('index.html'), 422
    if not validate_url(input_url):
        flash('Некорректный URL', 'danger')
        return render_template('index.html'), 422
    url = normalize_url(input_url)
    url_data = get_url_name(url)
    if url_data:
        flash('Страница уже существует', 'info')
    else:
        url_data = add_url(url, date.today())
        flash('Страница успешно добавлена', 'success')
    id = url_data['id']
    return redirect(url_for('show_info_url', id=id), code=302)


@app.route('/urls')
def show_added_urls():
    urls = get_all_urls()
    for url in urls:
        data_check = get_all_check(url['id'])
        if data_check:
            url['created_at'] = data_check['created_at']
            url['status_code'] = data_check['status_code']
    return render_template('urls.html', urls=urls)


@app.route('/urls/<id>')
def show_info_url(id):
    url_data = get_url_id(id)
    checks = get_checks_url(id)
    return render_template('url.html', url=url_data, checks=checks)


@app.post('/urls/<id>/checks')
def check_url(id):
    url = get_url_id(id)['name']
    try:
        response = requests.get(url)
        response.raise_for_status()
        status_code = response.status_code
        h1, title, description = parse_response(response)
        add_checks_url(id, status_code, h1, title,
                       description, date.today())
        flash('Страница успешно проверена', 'success')
    except (Exception, requests.exceptions.ConnectionError, ConnectionError):
        flash('Произошла ошибка при проверке', 'danger')
    return redirect(url_for('show_info_url', id=id), code=302)


@app.post('/urls/checks')
def check_urls():
    check_all_urls.delay()
    flash('Процесс проверки страниц запущен', 'success')
    return redirect(url_for('show_added_urls'), code=302)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
