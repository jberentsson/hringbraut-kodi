#!/usr/bin/env python3
from hringbraut import Hringbraut

import xbmc
import xbmcgui
import xbmcplugin
import xmbcaddon

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('Hringbraut')

line1 = "Hello"
line2 = "WORLD"
line3 = "!!!"

xbmcgui.Dialog().ok(addonname, line1, line2, line3)
