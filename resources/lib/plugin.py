# -*- coding: utf-8 -*-
"""

    SPDX-License-Identifier: Unlicense
    See LICENSES/Unlicense for more information.
"""

try:
    from kodi_six import xbmc
    from kodi_six import xbmcaddon
    from kodi_six import xbmcgui
    from kodi_six import xbmcplugin
    from kodi_six import xbmcvfs
    from kodi_six.utils import *
except ImportError:
    import xbmc
    import xbmcaddon
    import xbmcgui
    import xbmcplugin
    import xbmcvfs

import routing

plugin = routing.Plugin()
addon = xbmcaddon.Addon(id='plugin.script.testing')


@plugin.route('/')
def main():
    """
    Plugin path: plugin://plugin.script.testing/

    Create a menu item for each testable item type

    - Folder
    - Playable Item
    - Unplayable Item
    """

    def create_menu_item(list_item, route, is_folder, is_playable):
        if isinstance(is_playable, bool):
            item.setProperty(key='IsPlayable', value=str(is_playable).lower())

        xbmcplugin.addDirectoryItem(handle=plugin.handle, url=plugin.url_for(func=route),
                                    listitem=list_item, isFolder=is_folder)

    # plugin://plugin.script.testing/folder
    item = xbmcgui.ListItem(label=addon.getLocalizedString(30010))  # label: Folder
    create_menu_item(list_item=item, route='folder', is_folder=True, is_playable=None)

    # plugin://plugin.script.testing/play
    item = xbmcgui.ListItem(label=addon.getLocalizedString(30011))  # label: Playable Item
    create_menu_item(list_item=item, route='play', is_folder=False, is_playable=True)

    # plugin://plugin.script.testing/action
    item = xbmcgui.ListItem(label=addon.getLocalizedString(30012))  # label: Unplayable Item
    create_menu_item(list_item=item, route='action', is_folder=False, is_playable=False)

    xbmcplugin.endOfDirectory(handle=plugin.handle, succeeded=True, cacheToDisc=False)


@plugin.route('/folder')
def folder():
    """
    Plugin path: plugin://plugin.script.testing/folder

    "Folder" menu item endpoint
    """

    # -- add code --

    xbmcplugin.endOfDirectory(handle=plugin.handle, succeeded=True, cacheToDisc=False)


@plugin.route('/play')
def play():
    """
    Plugin path: plugin://plugin.script.testing/play

    "Playable Item" menu item endpoint
    """

    # -- add code --

    list_item = xbmcgui.ListItem(label=addon.getLocalizedString(30011))  # label: Playable Item
    list_item.setProperty(key='IsPlayable', value='true')
    list_item.setPath(path='')  # add path

    # -- add code --

    xbmcplugin.setResolvedUrl(handle=plugin.handle, succeeded=True, listitem=list_item)


@plugin.route('/action')
def action():
    """
    Plugin path: plugin://plugin.script.testing/action

    "Unplayable Item" menu item endpoint
    """

    # -- add code --

    pass
