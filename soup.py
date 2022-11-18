from bs4 import BeautifulSoup

# В HTML-коде не закрыт парный тег <p>.
simple_html = '<p>Закройте меня кто-нибудь!'
# Подставьте в одинарные кавычки разные features — 
# сначала html.parser, а потом lxml.
soup = BeautifulSoup(simple_html, features='lxml')
print(soup)