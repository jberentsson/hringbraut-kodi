#!/usr/bin/env python3
from hringbraut import Hringbraut

import xbmc
import xbmcgui
import xbmcplugin
import json

tv = Hringbraut()
shows = tv.get_shows()

for show in shows['shows']:
    item = xbmcgui.ListItem('%s' % show['text'])
    xbmcplugin.addDirectoryItem(int(sys.argv[1]), '', item, isFolder=0)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
