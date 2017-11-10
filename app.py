#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen

import re

class Hringbraut:
    def __init__(self):
        url = urlopen('http://hringbraut.is/sjonvarp')
        self.soup = BeautifulSoup(url, 'html.parser')

    def get_shows(self):
        s = self.soup.find(id="box_sitemap_47").find(id="subnavigation-23")
        for link in s.find_all('a'):
            l = link.get('href')
            t = link.get_text()
            if (l and t) and '/thaettir/' in l:
                print('%s %s' % (t, l))

if __name__ == "__main__":
    h = Hringbraut()
    h.get_shows()
