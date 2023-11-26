from flask import (Flask, render_template, request, flash, redirect, url_for)
import os
from datetime import date
from dotenv import load_dotenv
from page_analyzer.url_processing import validate_url, normalize_url
from page_analyzer.database import (get_url_name, add_url, get_url_id,
                                    get_all_urls)


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
    return render_template('urls.html', urls=urls)


@app.route('/urls/<id>')
def show_info_url(id):
    url_id = get_url_id(id)
    id = id
    name = url_id['name']
    created_at = url_id['created_at']
    return render_template('url.html', id=id, name=name,
                           created_at=created_at)

