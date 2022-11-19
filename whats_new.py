import requests_cache
from bs4 import BeautifulSoup

WHATS_NEW_URL = 'https://docs.python.org/3/whatsnew/'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(WHATS_NEW_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    main_div = soup.find('section', attrs={'id': 'what-s-new-in-python'})
    div_with_ul = main_div.find('div', attrs={'class': 'toctree-wrapper'})
    section_by_python = div_with_ul.find_all('li', attrs={'class': 'toctree-l1'})
    for section in section_by_python:
        version_a_tag = section.find('a')
        print(version_a_tag)