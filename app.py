#!/usr/bin/env python3
from hringbraut import Hringbraut

import xbmc
import xbmcgui
import xbmcplugin
import json
import urlparse
import urllib

tv = Hringbraut()
shows = tv.get_shows()

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])

args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'episodes')

params = dict(urlparse.parse_qsl(sys.argv[2][1:]))
action_key = params.get("action_key")
action_value = params.get("action_value")
name = params.get("name")
mode = args.get('mode', None)

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def main():
    # List the shows.
    for i, show in enumerate(shows['shows']):
        item = xbmcgui.ListItem('%s' % show['text'])
        url = build_url({'mode':'show', 'url':show['url']}) 
        xbmcplugin.addDirectoryItem(addon_handle, url, item, isFolder=True)
    xbmcplugin.endOfDirectory(addon_handle)

def show(url):
    # List the episodes.
    episodes = tv.get_show(url)
    for e in episodes['show']['episodes']:
        item = xbmcgui.ListItem('%s - %s' % e['date'], e['text'])
        xbmcplugin.addDirectoryItem(addon_handle, '', item, isFolder=False)
    xbmcplugin.endOfDirectory(addon_handle)


if mode is None:
    main()

elif mode[0] == 'show':
    url=args['url'][0]
    show(url)
