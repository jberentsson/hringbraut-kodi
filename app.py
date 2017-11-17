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

line1 = "WORLD"
line2 = json.dumps(shows)
line3 = "!!!"

xbmcgui.Dialog().ok(line1, line2, line3)
