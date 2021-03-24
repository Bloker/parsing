from bs4 import BeautifulSoup as bs
import requests


url = 'https://office-burg.ru/categories/'


def get_html(url):
    req = requests.get(url)
    if req.status_code == 200:
        return req.text
    else:
        print('Страница не доступна')


def get_categories(html):
    soup = bs(html, 'lxml')
    categories_link = soup.find_all('div', class_ = 'Categorie')
    print(categories_link)




print(get_categories(get_html(url)))