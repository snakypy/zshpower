.. image:: https://raw.githubusercontent.com/snakypy/snakypy-static/master/zshpower/logo/png/zshpower.png
    :width: 505 px
    :align: center
    :alt: ZSHPower

.. image:: https://github.com/snakypy/zshpower/workflows/Python%20package/badge.svg
    :target: https://github.com/snakypy/zshpower

.. image:: https://img.shields.io/pypi/v/zshpower.svg
    :target: https://pypi.python.org/pypi/zshpower

.. image:: https://travis-ci.com/snakypy/zshpower.svg?branch=master
    :target: https://travis-ci.com/snakypy/zshpower

.. image:: https://img.shields.io/pypi/wheel/zshpower
    :alt: PyPI - Wheel

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. image:: https://pyup.io/repos/github/snakypy/zshpower/shield.svg
    :target: https://pyup.io/repos/github/snakypy/zshpower/
    :alt: Updates

.. image:: https://img.shields.io/github/issues-raw/snakypy/zshpower
    :alt: GitHub issues

.. image:: https://img.shields.io/github/license/snakypy/zshpower
    :alt: GitHub license
    :target: https://github.com/snakypy/zshpower/blob/master/LICENSE


`ZSHPower` is a theme for `Oh My Zsh`_ framework; especially
for the `Python`_ developer. Pleasant to look at, the **ZSHPower**
comforts you with its colors and icons vibrant.

Installing **ZSHPower** is the easiest thing you will see in any existing theme for Oh My Zsh,
because ZSHPower has its own manager. With `ZSHPower`_,
changes to the theme become more dynamic through a configuration file, where the user can make various combinations
of changes, such as: **enable**, **disable**, **open settings**, **reset settings**, **uninstall** and more;
all in a simplified command line, without opening any files or creating symbolic links.
In addition, the **ZSHPower** manager downloads **Oh My Zsh** and the
`zsh-autosuggestions`_ and `zsh-syntax-highlighting`_ plugins automatically, everything to make your ZSH very power.


Requirements
------------

To work correctly, you will first need:

* `git`_ (v2.25 or recent) must be installed.
* `zsh`_  (v5.2 or recent) must be installed.
* `python`_ (v3.7 or recent) must be installed.
* `pip`_ (v19.3 or recent) must be installed.
* `nerd fonts`_ must be installed.


Features
--------

* `Oh My Zsh`_ Installation Automatically;
* Automatically install `zsh-autosuggestions`_ and `zsh-syntax-highlighting`_;
* Automated installation and uninstallation;
* Enable and disable `ZSHPower` anytime;
* Upgrade `ZSHPower` effortlessly;
* Reset the settings with one command only;
* Current Git branch and rich repo status:
    *  — untracked changes;
    *  — new files added;
    *  — deleted files;
    *  — new modified files;
    *  — commits made;
* Python version shown (*with pyenv support*) on the active virtual machine (E.g: `[python_icon] py-3.x`);
* Shows the version of the project if you use "**pyproject.toml**" (E.g: `[pkg_icon] 0.1.0`);
* Enables **username** and **hostname** when connecting with SSH. (can change in the settings to show permanently);
* and, many other dynamic settings in `$HOME/.config/snakypy/zshpower/config.toml`.


Installing
----------

Globally:

.. code-block:: shell

    $ sudo pip install zshpower

For the user:

.. code-block:: shell

    $ pip install zshpower --user


Using
-----

Because **ZSHPower** is a manager, usage information is in the
`ZSHPower`_ project. Access the project, and see how to use **ZSHPower**.

For more command information, run:

.. code-block:: shell

    $ zshpower --help

More information: https://github.com/snakypy/zshpower

Donation
--------

If you liked my work, buy me a coffee <3

.. image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
    :target: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YBK2HEEYG8V5W&source

License
-------

The gem is available as open source under the terms of the `MIT License`_ ©

Credits
-------

* Name: William C. Canin
* Country: Brazil - SP
* E-Mail: william.costa.canin@gmail.com
* Personal page: `William Canin`_

This package was created with Cookiecutter_ and the `williamcanin/pypkg-cookiecutter`_ project template.

Links
-----

* Code: https://github.com/snakypy/zshpower
* Documentation: https://github.com/snakypy/zshpower/blob/master/README.md
* Releases: https://pypi.org/project/zshpower/#history
* Issue tracker: https://github.com/snakypy/zshpower/issues

.. _Oh My Zsh: https://ohmyz.sh
.. _Python: https://python.org
.. _zsh-autosuggestions: https://github.com/zsh-users/zsh-autosuggestions
.. _zsh-syntax-highlighting: https://github.com/zsh-users/zsh-syntax-highlighting
.. _ZSHPower: https://github.com/snakypy/zshpower
.. _git: https://git-scm.com/downloads
.. _zsh: http://www.zsh.org/
.. _`python`: https://python.org
.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. _nerd fonts: https://www.nerdfonts.com/font-downloads
.. _MIT License: https://github.com/snakypy/zshpower/blob/master/LICENSE
.. _William Canin: http://williamcanin.github.io
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`williamcanin/pypkg-cookiecutter`: https://github.com/williamcanin/pypkg-cookiecutter
