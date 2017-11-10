#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen

import re

class Hringbraut:
    def __init__(self):
        url = urlopen('http://hringbraut.is/sjonvarp')
        self.soup = BeautifulSoup(url, 'html.parser')

    def get_shows(self):
        s = self.soup
        for link in s.find_all('a'):
            l = link.get('href')
            t = link.get_text()
            try:
                if l and t:
                    print('%s %s' % (t, l))
            except:
                return 0

if __name__ == "__main__":
    h = Hringbraut()
    h.get_shows()
