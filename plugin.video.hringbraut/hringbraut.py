#!/usr/bin/env python3
import logging
from bs4 import BeautifulSoup
from pprint import pprint

try:
    from urllib2 import urlopen
except:
    from urllib.request import urlopen

import re

logging.basicConfig(filename='/tmp/hringbraut.log',level=logging.DEBUG,  format='%(asctime)s - %(levelname)s - %(message)s')

class Hringbraut(object):
    """ Hringbraut Kodi addon. """
    def __init__(self):
        logging.info('Class created!')
        self.url = 'http://www.hringbraut.is'

    def read_url(self, url):
        """ Get the url data. """
        logging.info('Reading url: %s' % url)
        try:
            html = urlopen(url)
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        except:
            logging.warning('Error reading URL: %s' % url)

    def get_shows(self):
        """ Get the name and urls for the shows. """
        logging.info('Fetching shows.')
        try:
            soup = self.read_url(self.url + '/sjonvarp/')
            shows = []
            s = soup.find(id="box_sitemap_47")\
                    .find(id="subnavigation-23")

            for link in s.find_all('a'):
                url = link.get('href')
                text = link.get_text()
                if '/thaettir/' in url:
                    shows.append({
                        'text': text,
                        'url': url
                    })

            return {'shows': shows}
        except:
            logging.warning('Error fetching shows!')

    def get_show(self, url):
        """ Get all of the episodes of a show. """
        logging.info('Getting all episodes.')
        try:
            soup = self.read_url(self.url + url)
            s = soup.find(id='contentContainer')
            info = s.find('div', {'class':'channelDescription'})
            nav = s.find('div', {'class':'pagerContent'})

            return {
                    'show':{
                        'nav': {
                            'prev': self.get_nav(nav, 'previous'),
                            'next': self.get_nav(nav, 'next')
                        },
                        'episodes': self.get_episodes(s),
                        'name': self.get_title(info),
                        'description': self.get_description(info)
                        }
                    }
            
        except:
            logging.warning('Unable to get episodes!')
            return None

    def get_nav(self, nav, direction):
        """ Get the navigation urls. """
        logging.info('Fetching nav url.')
        try:
            out = nav.find('a', {'class': direction})
            out = str(out).split('"') # Not sure why I had to do this?
            return out[3]
        except:
            logging.info('No nav url found.')
            return None

    def get_episodes(self, soup):
        """ Get all of the episodes for a show. """
        logging.info('Fetch all episodes.')
        try:
            episodes=[]
            thumbs = soup.find(id='tube')\
                    .find('div', {'class':'row'})\
                    .find_all('div', {'class':'videoThumb'})

            for t in thumbs:
                episodes.append({
                    'text': t.find('h3')\
                             .get_text(),
                    'url': t.find('a')\
                            .get('href'),
                    'thumb': t.find('img')\
                              .get('src'),
                    'date': t.find('span', {'class': 'date'})\
                             .get_text(),
                })

            return episodes
        except:
            logging.warning('No episodes!')
            return None

    def get_title(self, soup):
        """ Get the name of the show. """
        logging.info('Fetching title.')
        try:
            return soup.find('h2').get_text()
        except:
            logging.warning('No title found!')
            return "~NAME MISSING~"

    def get_description(self, soup):
        """ Get show description. """
        logging.info('Fetching description!')
        try:
            desc = soup.find_all('p')
            return desc[0].get_text() + " " + desc[1].get_text()
        except:
            logging.warning('Description missing!')
            return "~Description MISSING~"

    def get_episode(self, url):
        """ Get the youtube url for an episode. """
        logging.info('Fetching episode stuff.')
        try:
            soup = self.read_url(self.url + url)
            return soup.find('iframe')\
                       .get('src')\
                       .split('?')[0]\
                       .split('/')[-1]
        except:
            logging.warning('No url found!')
            return None

if __name__ == "__main__":
    h = Hringbraut()    
    out = h.get_show('/sjonvarp/thaettir/man/')
