<h1 align="center">
  <a href="https://github.com/snakypy/zshpower">
    <img alt="ZSHPower" src="https://raw.githubusercontent.com/snakypy/snakypy-static/master/zshpower/logo/png/zshpower.png" width="505">
  </a>
  <br> ZSHPower - A powerful theme for <a href="https://ohmyz.sh" target="_blank"><code>Oh My ZSH</code></a><br>
</h1>

![Python package](https://github.com/snakypy/zshpower/workflows/Python%20package/badge.svg) [![Build Status](https://travis-ci.com/snakypy/zshpower.svg?branch=master)](https://travis-ci.com/snakypy/zshpower) [![Updates](https://pyup.io/repos/github/snakypy/zshpower/shield.svg)](https://pyup.io/repos/github/snakypy/zshpower/) [![Python 3](https://pyup.io/repos/github/snakypy/zshpower/python-3-shield.svg)](https://pyup.io/repos/github/snakypy/zshpower/) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/zshpower) ![PyPI](https://img.shields.io/pypi/v/zshpower) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/zshpower) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![PyPI - Downloads](https://img.shields.io/pypi/dm/zshpower) [![GitHub license](https://img.shields.io/github/license/snakypy/zshpower)](https://github.com/snakypy/zshpower/blob/master/LICENSE)

<div align="center">
  <h4>
    | <a href="https://snakypy.github.io">Website</a> |
    <a href="#features">Features</a> |
    <a href="#requirements">Requirements</a> |
    <a href="#installing">Install</a> |
    <a href="#post-install">Post-Install</a> |
    <a href="#theme-configuration">Theme configuration</a> |
    <a href="#reset-settings">Reset settings</a> |
    <a href="#upgrading">Upgrade</a> |
    <a href="#disable-and-enable">Disable/Enable</a> |
    <a href="#uninstalling">Uninstall</a> |
    <a href="#donation">Donation</a> |
  </h4>
  <h5>
    | <a href="#more-commands">More Commands</a> |
  </h5>
</div>

<div align="center">
  <sub>Built with ❤︎ by:
  <a href="https://williamcanin.github.io" target="_blank">William Canin</a> in free time,
  to the sound of the playlist: <a href="https://open.spotify.com/playlist/48brJJZdVifY79QAFmEImq?si=GmsvfKqATpG4p72ZeVClIQ" target="_blank">Bursting Of The Tympanum</a></sub>
</div>
<br>
<br>

`ZSHPower` is a theme for [Oh My Zsh](https://ohmyz.sh) framework; especially for the [Python](https://www.python.org/) developer. Pleasant to look at, the **ZSHPower**comforts you with its colors and icons vibrant.

Installing **ZSHPower** is the easiest thing you will see in any existing theme for Oh My Zsh,
because ZSHPower has its own manager. With **ZSHPower**,
changes to the theme become more dynamic through a configuration file, where the user can make various combinations
of changes, such as: **enable**, **disable**, **open settings**, **reset settings**, **uninstall** and more;
all in a simplified command line, without opening any files or creating symbolic links.
In addition, the **ZSHPower** manager downloads **Oh My Zsh** and the
[`zsh-autosuggestions`](https://github.com/zsh-users/zsh-autosuggestions) and [`zsh-syntax-highlighting`](https://github.com/zsh-users/zsh-syntax-highlighting) plugins automatically, everything to make your ZSH very power.

Here is an example of the installed **ZSHPower**:

<p align="center">
  <img alt="ZSHPower in Terminator" src="https://raw.githubusercontent.com/snakypy/snakypy-static/master/zshpower/demo/gifs/demo.gif" width="980px">
</p>

## Contributions

[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/0)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/0)[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/1)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/1)[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/2)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/2)[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/3)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/3)[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/4)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/4)[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/5)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/5)[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/6)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/6)[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/7)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/7)

## Features

- [Oh My Zsh](https://ohmyz.sh) Installation Automatically;
- Automatically install [`zsh-autosuggestions`](https://github.com/zsh-users/zsh-autosuggestions) and [`zsh-syntax-highlighting`](https://github.com/zsh-users/zsh-syntax-highlighting);
- Automated installation and uninstallation;
- Enable and disable `ZSHPower` anytime;
- Open configuration file in the terminal itself;
- Reset the settings with one command only;
- Current Git branch and rich repo status;
  - untracked changes;
  - new files added;
  - deleted files;
  - new modified files;
  - commits made;
- Python version shown (*with pyenv support*) on the active virtual machine (E.g: `[python_logo] 3.x`);
- Shows the version of the project if you use "**pyproject.toml**" (E.g: [package_logo] 0.1.0);
- Enables **username** and **hostname** when connecting with SSH. (can change in the settings to show permanently);
- and, many other dynamic settings in ```$HOME/.config/snakypy/zshpower/<version>/config.toml```.

## Requirements

To work correctly, you will first need:

- [`Git`](https://git-scm.com/downloads) (v2.25 or recent) must be installed;
- [`Zsh`](http://www.zsh.org/) (v5.2 or recent) must be installed;
- [`Python`](https://python.org) (v3.7 or recent);
- [`Pip`](https://pip.pypa.io/en/stable/) (v19.3 or recent) must be installed;
- Some [`Nerd Font`](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/) font installed;
- One of that editor [vim](https://www.vim.org/), [nano](https://www.nano-editor.org/) or [emacs](https://www.gnu.org/software/emacs/) must be installed;


## Installing

**1** - It's time to install `ZSHPower` manager. To do this, do:

Globally:

```shell
# pip install zshpower
```
or

```shell
$ sudo pip install zshpower
```

For the user:

```shell
$ pip install zshpower --user -U
```

> NOTE: If you are installing to the user's local environment, be sure to add the environment variables to the `zshrc` file.

**2** - After installing the package, you need to install the theme (`zshpower`) on the machine and its dependencies, for that do:

```shell
$ zshpower init
```

## Post-Install

The `ZSHPower` project uses the ["Nerd Font"](https://www.nerdfonts.com/font-downloads). You must install any of these fonts to terminally recognize the symbols.

However, by default, `ZSHPower` already downloads the font [**DejaVuSansMono Nerd Font**](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/DejaVuSansMono) in the folder (`$HOME/.fonts`) of user fonts using **Linux**  system.

If you use **Mac OS X**, consider installing the font  [**manually**](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/DejaVuSansMono)  on your system.

### Editors, IDE and Terminal

After `ZSHPower` installs the `DejaVuSansMono Nerd Font` font, you must configure your text editor and terminal to recognize the icons used by the `Snnapypy Prompt`.

**Visual Studio Code:**

Add the font family in [`Visual Studio Code`](https://code.visualstudio.com/),
opening the global settings for `Visual Studio Code` and add this information:

```json
"terminal.integrated.fontFamily": "'<Your main source>', 'DejaVuSansMono Nerd Font'",
```

**Atom:**

For the [Atom](https://atom.io/) editor, there are no secrets either. In the family font settings, do:

```cson
editor:
    fontFamily: "Menlo, Consolas, DejaVu Sans Mono, monospace, DejaVuSansMono Nerd Font"
```

**PyCharm:**

For [PyCharm](https://www.jetbrains.com/pycharm/), you must make the following font settings:

```
File > Settings > Editor > Color Schema > Console Font > Font: DejaVuSansMono Nerd Font
```

**Terminator:**

If you use [`Terminator`](https://terminator-gtk3.readthedocs.io/en/latest/) as the default terminal, change its font to the `DejaVuSansMono Nerd Font Book` font.

For other terminals, do the same, changing the font to `DejaVuSansMono Nerd Font Book`.

> NOTE: You can install any font from ["Nerd Font"](https://www.nerdfonts.com/font-downloads). They are compatible with the `ZSHPower`.

## Theme configuration

### About

**ZSHPower** allows you to open its settings in the terminal itself using **vim**, **nano** or **emacs**. After exiting the editor, *ZSHPower* will reload the settings in case there are any changes, it will take effect.

```shell
$ zshpower config --open
```

In the keys containing the call "**color**", you must enter a color that is in accordance with [Ansi Escape Color](https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit) . By default, the supported values are:

```shell
black|white|blue|red|cyan|magenta|green|yellow
```

The "**enable**" keys must receive Boolean values supported by TOML. The values for these keys are **true** or **false** (In lower case).

The **symbol** keys, receive icons or their values in `Unicode`. By default, the icons will only be shown via localhost, if the connection is via SSH, the icons will be disabled.

### Configuration file

The configuration file is found in **[HOME USER]/.config/snakypy/zshpower/[VERSION]/config.toml**, where in **VERSION** is the current version of **ZSHPower**.

```shell
$ zshpower --version
```

Know the file and its settings:

**General**:

```toml
[general]
jump_line.enable = true
separator.element = "-"
separator.color = "white"
position = ["package", "virtualenv", "python", "git"]
```

* **jump_line.enable** - If this option is `true`, you will skip a line each time you execute a command. `Default:` *true*

* **separator.element** - Add separators to each information shown by ZSHPower. `Default:` *"- "*

* **separator.color** - Changes the color of the separator. `Default:` *white*

* **position** -  This option changes the position of certain sections. *Default:* ["package", "virtualenv", "python", "git"]



**Username**:

```toml
[username]
enable = false
color = "cyan"
```

* **enable** - If it is active, it will show the username of the machine. When using SSH, even with the value `false` the username will be shown. `Default:` *false*

* **color** - Changes the color of the username. `Default:` *cyan*



**Hostname**:

```toml
[hostname]
enable = false
color = "magenta"
prefix.color = "green"
prefix.text = "at"
```

* **enable** -  If it is active, it will show the hostname of the machine. When using SSH, even with the value `false` the hostname will be shown.  `Default:` *false*
* **color** - Changes the color of the username.   `Default:` *magenta*
* **prefix.color** - Changes the color of the hostname prefix.  `Default:` *green*
* **prefix.text** - Before showing the hostname of the machine, it will have a prefix text. In this option you can change the text you want. `Default:` *at*



**Directory:**

```toml
[directory]
truncation_length = 2
symbol = "\ufc6e"
color = "cyan"
prefix.color = "green"
prefix.text = "in"
```

* **truncation_length** - This option receives an integer from 1 to 3. You will be responsible for truncating the path levels of the directory. `Default:` *2*
* **symbol** - Must receive an icon, whether in unicode or not. `Default:` \ufc6e
* **color** - Changes the color of the path.  `Default:` cyan
* **prefix.color** - Changes the color of the path prefix.   `Default:` *green*
* **prefix.text** - Before showing the current path (or folder), it will have prefixed text. In this option you can change the text you want. `Default:` *in*



**Git:**

```toml
[git]
enable = true
symbol = "\uf418"
color.symbol = "white"
branch.color = "cyan"
prefix.color = "green"
prefix.text = "on"
```

* **enable** -  If it is `true`, it will show git information if it is in a directory started with git. `Default:` *true*

* **symbol** - Must receive an icon, whether in unicode or not. `Default:` \uf418

* **color.symbol** - Option to change the color of the informed symbol. `Default:` *white*

* **branch.color** - Option to change the color of the informed branch. `Default:` *cyan*

* **prefix.color** - Changes the color of the prefix.   `Default:` *green*

* **prefix.text** - Before showing the git information, it will have prefixed text. In this option you can change the text you want. `Default:` *on*



**Git Status:**

```toml
[git.status]
symbols.enable = true
symbol.clean = "\uf62c"
symbol.added = "\ufc03"
symbol.modified = "\ufba8"
symbol.deleted = "\ufbc7"
symbol.renamed = "\uf101"
symbol.unmerged = "\uf6fb"
symbol.untracked = "\uf41e"
symbol.copied = "\ufab1"
symbol.ahead = "\uf55c"
symbol.behind = "\uf544"
symbol.diverged = "\ufb15"
symbol.conflicts = "\uf0e7"
```

* **symbols.enable** -  Receives `true` or` false`. If `true`, shows the git status icons through each defined value. Remember that these icons will not be shown if you are via SSH. `Default:` *true*



**Command**:

```toml
[command]
new_line.enable = true
symbol = "\uf553"
color = "green"
```

* **new_line.enable** - Receive `true` or` false`. If `true`, skip a line in the command entry. `Default:` *true*

* **symbol** - This option loads the arrow icon into the input. The input is where the commands in the terminal will be informed. You can use Unicode or the symbol.

  To find out which symbols and arrow unicode are supported by **ZSHPower**, visit [Nerd Font Cheat Sheet](https://www.nerdfonts.com/cheat-sheet) and search for `arrow` . `Default:` *\uf553*

* **color** - Changes the color of the input. `Default:` *green*



**Pyproject:**

```toml
[pyproject]
enable = true
symbol = "\uf8d6"
color = "magenta"
prefix.color = "green"
prefix.text = "on"
```

* **enable** - If the option is `true`, it will show the version information (with icon) of the Python project if it contains the file **pyproject.toml** in the directory.  `Default:` *true*
* **symbol** - Must receive an icon, whether in unicode or not. `Default:` \uf8d6
* **color** - Changes the color of the pyproject. `Default:` magenta
* **prefix.color** - Changes the color of the prefix.   `Default:` *green*
* **prefix.text** - Before showing the package information, it will have a prefixed text. In this option, you can change the text you want. `Default:` *on*



**Python:**

```toml
[python]
symbol = "\uf81f"
color = "yellow"
prefix.color = "green"
prefix.text = "via"
version.enable = true
version.micro.enable = true
```

* **symbol** - Must receive an icon, whether in unicode or not. `Default:` \uf81f
* **color** - Changes the color of the Python version information. `Default:` *yellow*
* **prefix.color** - Changes the color of the prefix.   `Default:` *green*
* **prefix.text** - Before showing the Python version information, it will have a prefixed text. In this option, you can change the text you want. `Default:` *via*
* **version.enable** - If it is `true`, it shows the version information of the Python currently used. Compatible with *Pyenv*.  `Default:` *true*
* **version.micro.enable** - If `true`, it will show the *MICRO* version of Python. Note: The `version.enable` key must be` true`. `Default:` *true*



**Virtualenv:**

```toml
[virtualenv]
enable = true
symbol = "\uf10c"
involved = "()"
color = "yellow"
prefix.color = "green"
prefix.text = "via"
```

* **enable** - If `true` displays the virtual machine information. `Default:` *true*
* **symbol** - Must receive an icon, whether in unicode or not. `Default:` \uf10c
* **involved** - Element that will involve the name of the virtual environment. By default, you should receive two single elements. `Default:` ()
* **color** - Changes the color of the virtual machine information. `Default:` yellow
* **prefix.color** - Changes the color of the prefix.   `Default:` *green*
* **prefix.text** - Before showing the virtual machine information, it will have a prefixed text. In this option, you can change the text you want. `Default:` `via`

```toml
[virtualenv.name]
normal.enable = true
text = "venv"
```

* **normal.enable** - If the option is `true`, it will show the real name of the virtual machine. If the option is `false`, the user has the possibility to enter text. `Default:` true
* **text** - Displays custom text in the name of the virtual machine. This option will only take effect if the `normal.enable` option has a value of  `false`. `Default:` *venv*



**Timer**

```toml
[timer]
enable = true
symbol = "\uf43a"
color = "blue"
seconds.enable = false
```

* **enable** - Receive `true` or` false`. If it has `true`, it shows a digital clock on the console.  `Default:` *true*
* **symbol** - Must receive an icon, whether in unicode or not. `Default:` \uf43a
* **color** - Changes the color of the clock.  `Default:` blue
* **seconds.enable** - Receive `true` or` false`. If it has `true`, show the seconds of the clock. `Default:` false



## Upgrading

If `ZSHPower` has any new features, please update the command line below:

Globally:

```shell
# pip install zshpower -U
$ zshpower init
```

or

```shell
$ sudo pip install zshpower -U
$ zshpower init
```
For the user:

```shell
$ pip install zshpower -U --user
$ zshpower init
```

## Reset settings

If you made any changes to the configuration file and regretted it, you can reset everything with the command below:

```shell
$ zshpower reset
```

## Disable and Enable

You can enable and disable `ZSHPower` anytime you want without opening any files. To do this, follow the steps below:

* Disable

```shell
$ zshpower disable
```

When disabled, the manager will return to the default [Oh My Zsh](https://github.com/robbyrussell/oh-my-zsh#selecting-a-theme) theme, the `robbyrussell`.
If you want to disable with another theme already installed, use the `--theme` option. Example:

```shell
$ zshpower disable --theme=agnoster
```

* Enable

```shell
$ zshpower enable
```

## Uninstalling

We will be sad if you want to stop using `ZSHPower`, but for easier uninstallation we also have the command:

```shell
$ zshpower uninstall
```

> NOTE:

If you installed "**ZSHPower**" with 'sudo', use 'sudo' to uninstall as well.

```shell
$ sudo zshpower uninstall
```

## More Commands

For more command information, use:

```
$ zshpower --help
```

## Donation

If you liked my work, buy me a coffee :coffee: :smiley:

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YBK2HEEYG8V5W&source)

## License

The project is available as open source under the terms of the [MIT License](https://github.com/snakypy/zshpower/blob/master/LICENSE) ©

## Credits

See, [AUTHORS](https://github.com/snakypy/zshpower/blob/master/AUTHORS.rst).
