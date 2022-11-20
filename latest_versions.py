import requests_cache
from bs4 import BeautifulSoup
import re

MAIN_DOC_URL = 'https://docs.python.org/3/'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(MAIN_DOC_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    sidebar = soup.find('div', attrs={'class': 'sphinxsidebarwrapper'})
    ul_tags = soup.find_all('ul')
    for ul in ul_tags:
        if 'All versions' in ul.text:
            a_tags = ul.find_all('a')
            break
    else:
        raise Exception('Ничего не нашлось')
    result = []
    pattern_r = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'
    for a_tag in a_tags:
        text_match = re.search(pattern_r, a_tag.text)
        link = a_tag['href']
        if text_match:
            version = text_match.group(1)
            status = text_match.group(2)
        else:
            version = a_tag.text
            status = ''
        result.append(
            (link, version, status)
        )
    for row in result:
        print(*row)