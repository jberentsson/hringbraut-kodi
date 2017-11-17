#!/usr/bin/env python3
from hringbraut import Hringbraut

import xbmc
import xbmcgui
import xbmcplugin
import json
import hringbraut

tv = hringbraut.Hringbraut()
shows = tv.get_shows()

#line2 = shows['shows'][1]['text']
username = "johann"

for show in shows['shows']:
    item = xbmcgui.ListItem('%s' % show['text'])
    xbmcplugin.addDirectoryItem(int(sys.argv[1]), '', item, isFolder=0)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
