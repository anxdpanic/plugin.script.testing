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

    def create_menu_item(label, route, is_folder, is_playable):
        item = xbmcgui.ListItem(label=label)

        if isinstance(is_playable, bool):
            item.setProperty(key='IsPlayable', value=str(is_playable).lower())
            if is_playable:
                item.setInfo('video', {'title': label})

        xbmcplugin.addDirectoryItem(handle=plugin.handle, url=plugin.url_for(func=route),
                                    listitem=item, isFolder=is_folder)

    create_menu_item(label='playable1. PlayMedia(plugin://) Crashes', route=play1, is_folder=False,
                     is_playable=True)
    create_menu_item(label='playable2. PlayMedia(http://) Doesn\'t Crash', route=play2, is_folder=False,
                     is_playable=True)
    create_menu_item(label='unplayable1. PlayMedia(plugin://) Doesn\'t Crash', route=action1, is_folder=False,
                     is_playable=False)

    xbmcplugin.endOfDirectory(handle=plugin.handle, succeeded=True, cacheToDisc=False)


@plugin.route('/play1')
def play1():
    """
        ********* CRASHES
    """

    playable_path = 'plugin://plugin.video.youtube/play/?video_id=5Lxu75r3-kI'

    # -- add code --

    list_item = xbmcgui.ListItem(label=addon.getLocalizedString(30011))  # label: Playable Item
    list_item.setInfo('video', {'title': addon.getLocalizedString(30011)})
    list_item.setProperty(key='IsPlayable', value='true')
    list_item.setPath(path=playable_path)  # add path
    # -- add code --
    xbmc.executebuiltin('PlayMedia(%s)' % playable_path)  # this shouldn't be called from a playable item, but also shouldn't crash when it's a plugin:// url

    xbmcplugin.setResolvedUrl(handle=plugin.handle, succeeded=True, listitem=list_item)  # crashes with or without this


@plugin.route('/play2')
def play2():
    """
        ********* DOESN'T CRASH
    """

    playable_path = 'https://download.blender.org/peach/bigbuckbunny_movies/BigBuckBunny_320x180.mp4'

    # -- add code --

    list_item = xbmcgui.ListItem(label=addon.getLocalizedString(30011))  # label: Playable Item
    list_item.setInfo('video', {'title': addon.getLocalizedString(30011)})
    list_item.setProperty(key='IsPlayable', value='true')
    list_item.setPath(path=playable_path)  # add path
    # -- add code --
    xbmc.executebuiltin('PlayMedia(%s)' % 'http://download.blender.org/ED/ed3d_sidebyside-RL-2x1920x1038_24fps.mkv')  # this shouldn't be called from a playable item, but also shouldn't crash when it's a plugin:// url

    xbmcplugin.setResolvedUrl(handle=plugin.handle, succeeded=True, listitem=list_item)


@plugin.route('/action1')
def action1():
    """
        ********* DOESN'T CRASH
    """

    xbmc.executebuiltin('PlayMedia(%s)' % 'plugin://plugin.video.youtube/play/?video_id=5Lxu75r3-kI')


if __name__ == '__main__':
    plugin.run()
