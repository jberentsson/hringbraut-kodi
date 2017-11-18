#!/usr/bin/env python3
from hringbraut import Hringbraut
import urlresolver
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
        item = xbmcgui.ListItem('%s - %s' % (e['date'], e['text']))
        url = build_url({'mode':'play', 'url':e['url']}) 
        xbmcplugin.addDirectoryItem(addon_handle, url, item, isFolder=False)
    xbmcplugin.endOfDirectory(addon_handle)

def play(video_id):
    path = 'plugin://plugin.video.youtube/play/?video_id=%s' % tv.get_episode(video_id)
    #item = xbmcgui.ListItem(path=playback_url)
    #xbmcplugin.setResolvedUrl(addon_handle, True, item)

    play_item = xbmcgui.ListItem(path=path)
    vid_url = play_item.getfilename()
    stream_url = resolve_url(vid_url)
    if stream_url:
    play_item.setPath(stream_url)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)

    #item = xbmcgui.ListItem('%s' % playback_url)
    #xbmcplugin.addDirectoryItem(addon_handle, '', item, isFolder=False)
    #xbmcplugin.endOfDirectory(addon_handle)

def resolve_url(url):
    duration=7500 #in milliseconds
    message = "Cannot Play URL"
    stream_url = urlresolver.HostedMediaFile(url=url).resolve()
    # If urlresolver returns false then the video url was not resolved.
    if not stream_url:
        dialog = xbmcgui.Dialog()
        dialog.notification("URL Resolver Error", message, xbmcgui.NOTIFICATION_INFO, duration)
        return False
    else: 
        return stream_url

if mode is None:
    main()

elif mode[0] == 'show':
    url=args['url'][0]
    show(url)

elif mode[0] == 'play':
    url=args['url'][0]
    play(url)
