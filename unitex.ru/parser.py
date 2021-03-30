from bs4 import BeautifulSoup as bs
import requests


def get_html(url):
    headers = {
        'accept': 'text/html, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }

    req = requests.get(url=url, headers=headers)
    if req.status_code == 200:
        # print(req.status_code)
        return req.text
    else:
        print('Страница не доступна')


def get_categories(html):
    soup = bs(html, 'lxml')
    categories_areas = soup.find('div', class_='right-bar').find_all('div', class_ = 'data')
    # for
    print(categories_areas[3])


def main():
    url = 'https://khanty-mansiysk.unitex.ru/office/'
    get_categories(get_html(url))


if __name__ == '__main__':
    main()

