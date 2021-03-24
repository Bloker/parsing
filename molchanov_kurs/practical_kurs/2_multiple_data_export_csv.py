import requests
from bs4 import BeautifulSoup as bs
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def refined(s):
    '''
    in -> 1,874 total ratings
    out - > 1874
    '''
    r = s.split(' ')[0]
    result = r.replace(',','')
    return result

def write_csv(data):
    with open('plugins.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'],
                         data['url'],
                         data['reviews']))


def get_data(html):
    soup = bs(html, 'lxml')
    popular = soup.find_all('section')[3]
    plugins = popular.find_all('article')
    for plugin in plugins:
        name = plugin.find('h3').text
        url = plugin.find('h3').find('a').get('href')
        r = plugin.find('span', class_ = 'rating-count').find('a').text
        rating = refined(r)
        data = {
            'name': name,
            'url': url,
            'reviews': rating
        }

        write_csv(data)

    # return data


def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
