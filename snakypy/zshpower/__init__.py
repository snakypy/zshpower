"""
ZSHPower
~~~~~~~~

ZSHPower is a theme for ZSH with a manager.


For more information, access: 'https://github.com/snakypy/zshpower'

:copyright: Copyright 2020-2021 by Snakypy team, see AUTHORS.
:license: MIT license, see LICENSE for details.
"""

from contextlib import suppress
from os.path import abspath, dirname, join
from pathlib import Path

from snakypy.helpers.files import eqversion

with suppress(KeyboardInterrupt):
    HOME = str(Path.home())
    __info__ = {
        "name": "ZSHPower",
        "version": "0.11.3",
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
                "website": "https://williamcanin.github.io",
                "locale": "Brazil - SP",
            }
        ],
    }

# Keep the versions the same on pyproject.toml and __init__.py
pyproject = join(dirname(abspath(__file__)), "../..", "pyproject.toml")
eqversion(pyproject, __info__["version"])
