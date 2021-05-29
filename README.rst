.. image:: https://raw.githubusercontent.com/snakypy/snakypy-static/master/zshpower/logo/png/zshpower.png
    :width: 505 px
    :align: center
    :alt: ZSHPower

_________________

.. image:: https://github.com/snakypy/zshpower/workflows/Tests/badge.svg
    :target: https://github.com/snakypy/zshpower

.. image:: https://img.shields.io/pypi/v/zshpower.svg
    :target: https://pypi.python.org/pypi/zshpower
    :alt: PyPI - ZSHPower

.. image:: https://img.shields.io/pypi/wheel/zshpower
    :target: https://pypi.org/project/wheel/
    :alt: PyPI - Wheel

.. image:: https://img.shields.io/pypi/pyversions/zshpower
    :target: https://pyup.io/repos/github/snakypy/zshpower/
    :alt: Python versions

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Black

.. image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
    :target: https://pycqa.github.io/isort/
    :alt: Isort

.. image:: http://www.mypy-lang.org/static/mypy_badge.svg
    :target: http://mypy-lang.org/
    :alt: Mypy

.. image:: https://pyup.io/repos/github/snakypy/zshpower/shield.svg
   :target: https://pyup.io/repos/github/snakypy/zshpower/
   :alt: Updates

.. image:: https://img.shields.io/github/issues-raw/snakypy/zshpower
    :target: https://github.com/snakypy/zshpower/issues
    :alt: GitHub issues

.. image:: https://img.shields.io/github/license/snakypy/zshpower
    :target: https://github.com/snakypy/zshpower/blob/master/LICENSE
    :alt: GitHub license

_________________

`ZSHPower` is a theme for ZSH; especially for the `Python`_ developer. Pleasant to look at, the **ZSHPower** comforts you with its colors and icons vibrant.

Installing **ZSHPower** is the easiest thing you will see in any existing theme for **ZSH**, because there is a manager.

The changes in the theme become more dynamic through a configuration file, where the user can make various combinations for the style of **ZSHPower**.

The **ZSHPower** supports installation along with `Oh My ZSH`_, where changes to: **enable** and **disable** an `Oh My ZSH`_ theme are easier, all in a simplified command line, without opening any files or creating symbolic links.

In addition, the **ZSHPower** manager downloads **Oh My Zsh** and the
`zsh-autosuggestions`_ and `zsh-syntax-highlighting`_ plugins automatically, everything to make your ZSH very power.


Requirements
------------

To work correctly, you will first need:

* `git`_ (v2.25 or recent) must be installed.
* `zsh`_  (v5.2 or recent) must be installed.
* `python`_ (v3.9 or recent) must be installed.
* `sqlite3`_ (v3.35 or recent) must be installed.
* `pip`_ (v21.0.1 or recent) must be installed.
* `nerd fonts`_ must be installed.


Features
--------

* `Oh My Zsh`_ installation automatically;*
* Automatically install `zsh-autosuggestions`_ and `zsh-syntax-highlighting`_;
* Automated installation and uninstallation;
* Enable and disable `ZSHPower` anytime;
* Upgrade `ZSHPower` effortlessly;
* Reset the settings with one command only;
* Personalized directory with truncate option;
* Current Git branch and rich repo status:
    *  — untracked changes;
    *  — new files added;
    *  — deleted files;
    *  — new modified files;
    *  — commits made;
    *  — and more.
* Application versions shown with `nerd fonts`_, they are:
    * CMake, Crystal, Dart, Deno, Docker, Docker, Dotnet, Elixir, Erlang, Go, Gulp, Helm, Java, Julia, Kotlin, Nim, NodeJS, Ocaml, Perl, Php, Python, Ruby, Rust, Scala, Vagrant, Zig
* Package versions such as Crystal, Helm, NodeJS, Python, Rust shown;
* Shows the time in the upper right corner;
* and, many other dynamic settings in `$HOME/.zshpower/<VERSION>/config.toml`.

\* features if used with **Oh My ZSH**.


Installing
----------

Globally:

.. code-block:: shell

    $ sudo pip install zshpower

NOTE: It is not recommended to install globally.

For the user:

.. code-block:: shell

    $ pip install zshpower --user


Using
-----

Run the command below to set `ZSHPower`_ on your ZSH.

.. code-block:: shell

    $ zshpower init [--omz]

For more command information, run:

.. code-block:: shell

    $ zshpower --help

More information: https://github.com/snakypy/zshpower

Donation
--------

Click on the image below to be redirected the donation forms:

.. image:: https://raw.githubusercontent.com/snakypy/donations/master/svg/donate/donate-hand.svg
    :width: 160 px
    :height: 100px
    :target: https://github.com/snakypy/donations/blob/master/README.md


License
-------

The gem is available as open source under the terms of the `MIT License`_ ©

Credits
-------

See, `AUTHORS`_.

Links
-----

* Code: https://github.com/snakypy/zshpower
* Documentation: https://github.com/snakypy/zshpower/blob/master/README.md
* Releases: https://pypi.org/project/zshpower/#history
* Issue tracker: https://github.com/snakypy/zshpower/issues

.. _AUTHORS: https://github.com/snakypy/zshpower/blob/master/AUTHORS.rst
.. _Oh My Zsh: https://ohmyz.sh
.. _zsh-autosuggestions: https://github.com/zsh-users/zsh-autosuggestions
.. _zsh-syntax-highlighting: https://github.com/zsh-users/zsh-syntax-highlighting
.. _ZSHPower: https://github.com/snakypy/zshpower
.. _git: https://git-scm.com/downloads
.. _zsh: http://www.zsh.org/
.. _python: https://python.org
.. _sqlite3: https://www.sqlite.org
.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. _nerd fonts: https://www.nerdfonts.com/font-downloads
.. _MIT License: https://github.com/snakypy/zshpower/blob/master/LICENSE
.. _William Canin: http://williamcanin.github.io
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`williamcanin/pypkg-cookiecutter`: https://github.com/williamcanin/pypkg-cookiecutter
