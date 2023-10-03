# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 09:24:14 2023

@author: Lenovo
"""
import requests
from bs4 import BeautifulSoup

def parse_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    data = []

    for item in items:
        title = item.h4.get_text().strip()
        description = item.p.get_text().strip()
        price = item.h5.get_text().strip()

        data.append({
            'title': title,
            'description': description,
            'price': price,
        })

    return data

def crawl_all_pages(base_url):
    all_data = []
    page = 1

    while True:
        url = base_url.format(page)
        data = parse_page(url)

        if not data:
            break

        all_data.extend(data)
        page += 1

    return all_data

base_url = 'https://scrapingclub.com/exercise/list_basic/?page={}'
data = crawl_all_pages(base_url)

for item in data:
    print(item)
