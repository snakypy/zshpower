"""
ZSHPower
~~~~~~~~

ZSHPower is a theme for ZSH with a manager.


For more information, access: 'https://github.com/snakypy/zshpower'

:copyright: Copyright 2020-2020 by Snakypy team, see AUTHORS.
:license: MIT license, see LICENSE for details.
"""

try:
    from pathlib import Path

    HOME = str(Path.home())

    __version__ = "0.6.0"

except (KeyboardInterrupt):
    pass
