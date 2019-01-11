# -*- coding: utf-8 -*-
"""

    SPDX-License-Identifier: Unlicense
    See LICENSES/Unlicense for more information.

    Usage:
        RunScript(special://home/addons/plugin.script.testing/resources/lib/script.py,mode=main,param=value)

"""

import sys

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


def _get_args():
    args_dict = {'mode': None}
    if len(sys.argv) == 1:
        args_dict['mode'] = 'main'
    else:
        argv = [arg.split('=') for arg in sys.argv if len(arg.split('=')) == 2]
        for args in argv:
            args_dict[args[0].lower()] = args[1]
    return args_dict


def run():
    args = _get_args()
    if args['mode'] == 'main':
        # -- add code --
        pass

    # -- add code --


if __name__ == '__main__':
    run()
