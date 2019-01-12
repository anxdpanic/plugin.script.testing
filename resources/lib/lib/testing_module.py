# -*- coding: utf-8 -*-
"""

    SPDX-License-Identifier: Unlicense
    See LICENSES/Unlicense for more information.

    Usage:
        -- addon.xml --
        <requires>
            <import addon="plugin.script.testing" version="0.0.1"/>
        ...

        -- <filename>.py --
        import testing_module
        ...

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
