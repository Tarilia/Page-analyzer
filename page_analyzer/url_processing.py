from urllib.parse import urlparse
from validators import url
from bs4 import BeautifulSoup


MAX_LEN_URL = 255


def validate_url(input_url):
    return url(input_url) and len(input_url) <= MAX_LEN_URL


def normalize_url(input_url):
    parsed_url = urlparse(input_url)
    return f'{parsed_url.scheme}://{parsed_url.netloc}'


def parse_response(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    h1 = soup.find('h1')
    title = soup.find('title')
    description = soup.find(attrs={'name': 'description'})
    h1 = h1.text.strip() if h1 else ''
    title = title.text.strip() if title else ''
    description = description['content'].strip() if description else ''
    return h1, title, description
