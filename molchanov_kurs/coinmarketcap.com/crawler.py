import requests
from bs4 import BeautifulSoup as bs
import csv
from datetime import datetime

from multiprocessing import Pool
import time


def get_html(url):
    r = requests.get(url)
    return r.text


def get_all_links():
    """Получает все ссылки на крипту"""
    url = 'https://coinmarketcap.com'
    links = []
    for page in range(1, 45):
        r = get_html(url + f'/?page={page}')
        soup = bs(r, 'lxml')
        tds = soup.find('table', class_='cmc-table').find_all('tr')
        for td in tds:
            if td.find('a', class_='cmc-link'):
                a = td.find('a', class_='cmc-link').get('href')
                link = url + a
                links.append(link)

    return links


def get_page_data(html):
    '''Парсим данные из сылок'''
    soup = bs(html, 'lxml')
    try:
        name = soup.find('h2', class_='sc-fzqBZW').text.strip()
    except:
        name = ''

    try:
        price = soup.find('div', class_='priceValue___11gHJ').text.strip()
    except:
        price = ''
    data = {
        'name': name,
        'price': price
    }

    return data


def write_csv(data):
    with open('coinmarketcup.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['price']))
        print(f'Спарсено: {data["name"]} - {data["price"]}')


def make_all(link):
    '''Для многопоточности'''
    html = get_html(link)
    data = get_page_data(html)
    write_csv(data)



def main():
    start = datetime.now()
    all_links = get_all_links()
    for link in all_links:
        html = get_html(link)
        data = get_page_data(html)
        write_csv(data)
        time.sleep(1)

    # Вызов многопоточности
    # with Pool(40) as p:
    #     p.map(make_all, all_links)

    end = datetime.now()
    total = end - start
    print(str(total))


if __name__ == '__main__':
    main()
