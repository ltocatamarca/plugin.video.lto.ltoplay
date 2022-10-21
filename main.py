# -*- coding: utf-8 -*-
# Module: plugin.video.lto.ltoplay
# Author: LTO Catamarca - @ltocatamarca
# Site: https://github.com/ltocatamarca/plugin.video.lto.ltoplay
# Created on: 2022-10-21

import sys
import xbmcgui
import xbmcplugin

_handle = int(sys.argv[1])



def mainlist():
    listing = []

    list_item = xbmcgui.ListItem(label='En vivo', iconImage='DefaultTVShows.png')
    url = 'https://ltocatamarca.github.io/ltotv.m3u8'
    list_item.setProperty('IsPlayable', 'true')
    list_item.setInfo(type='video', infoLabels={'title': 'LTO Television en vivo'})
    is_folder = False
    listing.append((url, list_item, is_folder))



    list_items(listing)


def list_items(listing):
    xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
    xbmcplugin.endOfDirectory(_handle)


if __name__ == '__main__':
    mainlist()
