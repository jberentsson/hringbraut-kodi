#!/usr/bin/env python3
import xbmc
import xbmcgui
import xbmcplugin
import json
import urlparse
import urllib

from hringbraut import Hringbraut


base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
params = dict(urlparse.parse_qsl(sys.argv[2][1:]))
name = params.get("name")
mode = args.get('mode', None)

xbmcplugin.setContent(addon_handle, 'episodes')

tv = Hringbraut()
shows = tv.get_shows()

def build_url(query):
    """ Creates the url for kodi. """
    return base_url + '?' + urllib.urlencode(query)

def main():
    """ List the shows. """
    for i, s in enumerate(shows['shows']):
        item = xbmcgui.ListItem('%s' % s['text'])
        url = build_url({
            'mode':'show',
            'url':s['url']
            })
        xbmcplugin.addDirectoryItem(addon_handle, url, item, isFolder=True)
    xbmcplugin.endOfDirectory(addon_handle)

def show(url):
    """ List the episodes. """
    episodes = tv.get_show(url)
    for e in episodes['show']['episodes']:
        item = xbmcgui.ListItem('%s - %s' % (e['date'], e['text']))
        url = build_url({
            'mode':'play',
            'url':e['url'],
            'name':"e['text']"
            })
        xbmcplugin.addDirectoryItem(addon_handle, url, item, isFolder=False)
    xbmcplugin.endOfDirectory(addon_handle)

def play(video_id, video_name):
    """ Play the video with the youtube plugin. """
    url = 'plugin://plugin.video.youtube/play/?video_id=%s' % tv.get_episode(video_id)
    xbmc.Player().play(url, xbmcgui.ListItem(video_name))

if mode is None:
    main()

elif mode[0] == 'show':
    url=args['url'][0]
    show(url)

elif mode[0] == 'play':
    url=args['url'][0]
    name=args['name'][0]
    play(url, name)
