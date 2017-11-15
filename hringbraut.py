#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
#from urllib.parse import 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 
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
            text = link.get_text()
            if '/thaettir/' in url:
                shows.append({'text': text, 'url': url})
                
        return {'shows': shows}

    def get_episodes(self, url):
        """ Get all of the episodes of a show. """
        html = urlopen(self.url + url)
        soup = BeautifulSoup(html, 'html.parser')

        episodes=[]
        s = soup.find(id='contentContainer')
        info = s.find('div', {'class':'channelDescription'})
        name = s.find('h2').get_text()
        desc = s.find_all('p')
        description = desc[0].get_text() + " " + desc[1].get_text()
        for link in s.find_all('a'):
            l = link.get('href')
            text = link.get_text().strip()
            if l != None:
                if url in l and url != l:
                    episodes.append({'text': text, 'url': l})
        return {'show':{'episodes': episodes, 'name': name, 'description': description}}

    def get_episode(self, url):
        """ Get the youtube url for an episode. """
        with urlopen(self.url + url) as response:
            html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        s = soup.find('iframe').get('src').split('?')[0].split('/')[-1]
        pprint(s)
        return s

if __name__ == "__main__":
    h = Hringbraut()    
    out = h.get_episodes('/sjonvarp/thaettir/man/')
