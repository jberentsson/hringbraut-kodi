#!/usr/bin/env python3
from kodijson import Kodi, PLAYER_VIDEO
from pprint import pprint
import json

import hringbraut

class innkodi:
    def get_conf(self):
        with open('config.json') as json_data:
            return json.load(json_data)

    def __init__(self):
        self.conf = self.get_conf()
        self.kodi = Kodi(self.conf['host'], self.conf['user'], self.conf['pass'])

        ping = self.kodi.JSONRPC.Ping()
        print(ping)

    def play_video(self, id):
        url = 'plugin://plugin.video.vimeo/play/?video_id='
        data = {
            "item":{
                "file":url + id
            }
        }

        self.kodi.Player.Open(data)

def print_shows():
    """ Print the id and name of show. """
    shows = tv.get_shows()

    i = 0
    for show in shows['shows']:
        #pprint(show)
        print("%s - %s" % (i, show['text']))
        i += 1

    return shows['shows']

def print_episodes(id):
    """ Print the id and name of the episodes """
    t = shows[id]['url']
    
    show = tv.get_episodes(t)
    #pprint(show)
    #print(show['show']['name'])
    #print(show['show']['description'])

    i = 0
    for episode in show['episodes']:
        if episode['url'][-1].split("/")[-1].isdigit() == False:
            print("%s - %s - %s" %(i, episode['text'], episode['url']))
            i += 1

    return show['episodes']

def get_id():
    try:
        id = input("Enter the show ID: ")
        return int(id)
    except:
        return None

if __name__=="__main__":
    kodi = innkodi()
    tv = hringbraut.Hringbraut()
    shows = print_shows()
    show = print_episodes(get_id()) 
    episode = tv.get_episode(show[get_id()]['url'])
    pprint(episode)

    #kodi.play_video(episode)