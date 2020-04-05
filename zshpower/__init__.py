"""
ZSHPower
~~~~~~~~

ZSHPower is a theme with a manager for the Oh My ZSH framework.


For more information, access: 'https://github.com/snakypy/zshpower'

:copyright: Copyright 2020-2020 by Snakypy team, see AUTHORS.
:license: MIT license, see LICENSE for details.
"""

from . import __name__
from pathlib import Path

HOME = str(Path.home())
__version__ = "0.2.6"
__pkginfo__ = {
    "name": "ZSHPower",
    "description": "ZSHPower is a theme with a manager for the Oh My ZSH framework.",
    "pkg_name": __name__,
    "executable": __name__,
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
            "website": "http://williamcanin.me",
            "locale": "Brazil - SP",
        }
    ],
}
