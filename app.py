#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen

import re

class Hringbraut:
    def __init__(self):
        url = urlopen('http://hringbraut.is/sjonvarp')
        self.soup = BeautifulSoup(url, 'html.parser')

    def get_shows(self):
        """ Get the name and urls for the shows. """
        shows = []
        s = self.soup.find(id="box_sitemap_47").find(id="subnavigation-23")
        for link in s.find_all('a'):
            url = link.get('href')
            name = link.get_text()
            if '/thaettir/' in url:
                shows.append({'name': name, 'url': url})
                
        return {'shows': shows}

if __name__ == "__main__":
    h = Hringbraut()
    out = h.get_shows()
    print(out)