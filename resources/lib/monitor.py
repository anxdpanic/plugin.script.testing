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


# noinspection PyPep8Naming
class Monitor(xbmc.Monitor):
    """ https://codedocs.xyz/xbmc/xbmc/group__python__monitor.html """

    def __init__(self, *args, **kwargs):
        xbmc.Monitor.__init__(self)

    def onSettingsChanged(self):
        pass

    def onScreensaverActivated(self):
        pass

    def onScreensaverDeactivated(self):
        pass

    def onDPMSActivated(self):
        pass

    def onDPMSDeactivated(self):
        pass

    def onScanStarted(self, library):
        pass

    def onScanFinished(self, library):
        pass

    def onDatabaseScanStarted(self, database):
        pass

    def onDatabaseUpdated(self, database):
        pass

    def onCleanStarted(self, library):
        pass

    def onCleanFinished(self, library):
        pass

    def onAbortRequested(self):
        pass

    def onNotification(self, sender, method, data):
        pass
