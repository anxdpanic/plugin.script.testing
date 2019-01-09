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

addon = xbmcaddon.Addon(id='plugin.script.testing')


class Player(xbmc.Player):
    """ https://codedocs.xyz/xbmc/xbmc/group__python___player_c_b.html """

    def __init__(self, *args, **kwargs):
        xbmc.Player.__init__(self)

    def onPlayBackStarted(self):
        pass

    def onAVStarted(self):
        pass

    def onAVChange(self):
        pass

    def onPlayBackEnded(self):
        pass

    def onPlayBackStopped(self):
        pass

    def onPlayBackError(self):
        pass

    def onPlayBackPaused(self):
        pass

    def onPlayBackResumed(self):
        pass

    def onQueueNextItem(self):
        pass

    def onPlayBackSpeedChanged(self):
        pass

    def onPlayBackSeek(self):
        pass

    def onPlayBackSeekChapter(self):
        pass
