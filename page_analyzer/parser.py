from bs4 import BeautifulSoup


def parse_response(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    h1 = soup.find('h1')
    title = soup.find('title')
    description = soup.find(attrs={'name': 'description'})
    h1 = h1.text.strip() if h1 else ''
    title = title.text.strip() if title else ''
    description = description['content'].strip() if description else ''
    return h1, title, description
