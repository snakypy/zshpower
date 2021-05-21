"""
ZSHPower
~~~~~~~~

ZSHPower is a theme for ZSH with a manager.


For more information, access: 'https://github.com/snakypy/zshpower'

:copyright: Copyright 2020-2021 by Snakypy team, see AUTHORS.
:license: MIT license, see LICENSE for details.
"""

from contextlib import suppress
from pathlib import Path

with suppress(KeyboardInterrupt):
    HOME = str(Path.home())
    __info__ = {
        "name": "ZSHPower",
        "version": "0.8.0",
        "description": "ZSHPower is a theme for ZSH with a manager.",
        "pkg_name": "zshpower",
        "executable": "zshpower",
        "home_page": "https://github.com/snakypy/zshpower",
        "organization_name": "Snakypy",
        "author": {
            "name": "William C. Canin",
            "email": "william.costa.canin@gmail.com",
            "website": "https://williamcanin.github.io",
            "github": "https://github.com/williamcanin",
        },
        "credence": [
            {
                "my_name": "William C. Canin",
                "email": "william.costa.canin@gmail.com",
                "website": "http://williamcanin.github.io",
                "locale": "Brazil - SP",
            }
        ],
    }
