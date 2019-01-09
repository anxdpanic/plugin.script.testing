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

if __name__ == '__main__':
    pass
