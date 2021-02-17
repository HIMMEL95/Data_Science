import requests
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0'
}

news = 'https://news.daum.net/breakingnews/'
html = requests.get(news, headers=headers).text
soup = bs(html, 'html.parser')

title = soup.select('#cSub > div > ul.tab_nav tab_nav2 > li > a')
print(title)
