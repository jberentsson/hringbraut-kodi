#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen

import re

class Hringbraut:
    def __init__(self):
        self.url = 'http://www.hringbraut.is'

    def get_shows(self):
        """ Get the name and urls for the shows. """
        html = urlopen(self.url + '/sjonvarp/')
        soup = BeautifulSoup(html, 'html.parser')
        shows = []
        s = soup.find(id="box_sitemap_47").find(id="subnavigation-23")
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
        #print(url)
        #for link in soup.find(id='tube').find_all('a'):
        #    print(link.get('href'))
        episodes=[]
        for link in soup.find(id='contentContainer').find_all('a'):
            l = link.get('href')
            if l != None:
                if url in l:
                    episodes.append(l)
        return episodes
                    

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
        #try:
        i = input("0 - 15: ")

        if 0 < int(i) < 16:
            out = self.get_shows()
            t = out['shows'][int(i)]['url']
            #print(t)
            out = self.get_episodes(t)
            print(out)

        self.main()
        #except:
        #    print("Error")

if __name__ == "__main__":
    h = Hringbraut()    
    #h.main()
    out = h.get_episodes('/sjonvarp/thaettir/man/')
    #print(out)
