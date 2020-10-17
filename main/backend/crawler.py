import requests
import csv
from bs4 import BeautifulSoup
from database import Database
import os

database = Database("data/products.db")

# create csv file with 2 columns
f = csv.writer(open('data/z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

def web_crawler():

    pages = []

    # populate initialized list
    for i in range(1, 5):
        url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
        pages.append(url)

    # this loop will go through each of the pages above
    for item in pages:
        page = requests.get(item)
        soup = BeautifulSoup(page.text, 'html.parser')

        # Remove bottom links
        last_links = soup.find(class_='AlphaNav')
        last_links.decompose()

        # Pull all text from the BodyText div and Pull text from all instances of <a> tag within BodyText div
        artist_name_list = soup.find(class_='BodyText')
        artist_name_list_items = artist_name_list.find_all('a')

        # loop to print out all artists' names
        for artist_name in artist_name_list_items:
            names = artist_name.contents[0]
            links = 'https://web.archive.org' + artist_name.get('href')

            f.writerow([names, links])
            database.insert(names, links)

web_crawler()