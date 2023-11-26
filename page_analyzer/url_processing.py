from urllib.parse import urlparse
from validators import url


MAX_LEN_URL = 255


def validate_url(input_url):
    return url(input_url) and len(input_url) <= MAX_LEN_URL


def normalize_url(input_url):
    parsed_url = urlparse(input_url)
    return f'{parsed_url.scheme}://{parsed_url.netloc}'
