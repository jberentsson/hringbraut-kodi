#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen

import re
from pprint import pprint

class Hringbraut:
    def __init__(self):
        self.url = 'http://www.hringbraut.is'

    def get_shows(self):
        """ Get the name and urls for the shows. """
        html = urlopen(self.url + '/sjonvarp/')
        soup = BeautifulSoup(html, 'html.parser')

        shows = []
        s = soup.find(id="box_sitemap_47")\
                .find(id="subnavigation-23")

        for link in s.find_all('a'):
            url = link.get('href')
            name = link.get_text()
            if '/thaettir/' in url:
                shows.append({'name': name, 'url': url})
                
        return {'shows': shows}

    def get_episodes(self, url):
        """ Get all of the episodes of a show. """
        html = urlopen(self.url + url)
        soup = BeautifulSoup(html, 'html.parser')

        episodes=[]
        s = soup.find(id='contentContainer')\
                .find_all('a')

        for link in s:
            l = link.get('href')
            name = link.get_text()
            if l != None:
                if url in l and url != l:
                    episodes.append({'name': name, 'url': l})
        return {'episodes': episodes}

    def get_episode(self, url):
        """ Get the youtube url for an episode. """
        html = urlopen(self.url + url)
        soup = BeautifulSoup(html, 'html.parser')

        return 'https:' + soup.find("iframe").get('src')
                    

    def print_shows(self):
        """ Print the show names to terminal. """
        shows = self.get_shows()
        i = 0
        for s in shows['shows']:
            print("%s %s" % (i, s['name']))
            i = i + 1

    def main(self):
        """ The main function. """
        self.print_shows()
        try:
            i = input("0 - 15: ")

            if 0 < int(i) < 16:
                out = self.get_shows()
                t = out['shows'][int(i)]['url']
                out = self.get_episodes(t)
                pprint(out)

            self.main()
        except:
            print("Error")

if __name__ == "__main__":
    h = Hringbraut()    
    out = h.get_episodes('/sjonvarp/thaettir/man/')
