#!/usr/bin/env python3
from kodijson import Kodi, PLAYER_VIDEO
from pprint import pprint
import json
import os

import hringbraut

class HringbrautKodi:
    """ Hringbraut Kodi addon testing. """
    def __init__(self):
        self.conf = self.get_conf()
        self.kodi = Kodi(self.conf['host'], self.conf['user'], self.conf['pass'])

    def get_conf(self):
        """ Get the config.json file. """
        with open('config.json') as json_data:
            return json.load(json_data)

    def play_video(self, id):
        """ Send the video to kodi. """
        try:
            url = 'plugin://plugin.video.youtube/play/?video_id='
            data = {
                "item":{
                    "file":url + id
                }
            }

            self.kodi.Player.Open(data)
        except:
            msg = "Unable to play video!"
            print(msg)

def print_shows():
    """ Print the id and name of show. """
    os.system('clear')
    shows = tv.get_shows()

    for i, show in enumerate(shows['shows']):
        print("%s - %s" % (i, show['text']))

    return shows['shows']

def print_episodes(id, shows):
    """ Print the id and name of the episodes """
    os.system('clear')
    t = shows[id]['url']

    show = tv.get_show(t)

    print(show['show']['name'])
    print(show['show']['description'])

    episodes = show['show']['episodes']

    for i, episode in enumerate(episodes):
        url = episode['url']
        text = episode['text']

        # TODO: refactor this.
        if url[-1].split("/")[-1].isdigit() == False:
            print("%s - %s - %s" %(i, text, url))

    return show['show']['episodes']

def get_id():
    """ Get the user input for the ID. """
    try:
        id = input("Enter the show ID: ")
        return int(id)
    except:
        return None

def loop():
    #try:
    os.system('clear')
    kodi = HringbrautKodi()
    shows = print_shows()
    show = print_episodes(get_id(), shows)
    episode = tv.get_episode(show[get_id()]['url'])
    pprint(episode)
    kodi.play_video(episode)
    loop()
    #except:
    #    msg = "Unable to do something!"
    #    print(msg)

if __name__=="__main__":
    tv = hringbraut.Hringbraut()
    loop()
