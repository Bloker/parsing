import requests
from bs4 import BeautifulSoup as bs


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = bs(html, 'lxml')
    h1 = soup.find('div', id='home-welcome').find('h1').text
    return h1


def main():
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
