from bs4 import BeautifulSoup
simple_html = '<p>Закройте меня кто-нибудь!'# Подставьте в одинарные кавычки разные features — 
soup = BeautifulSoup(simple_html, features='lxml')
print(soup)