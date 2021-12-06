<h1 align="center">
  <a href="https://github.com/snakypy/zshpower">
    <img alt="ZSHPower" src="https://raw.githubusercontent.com/snakypy/assets/master/zshpower/images/zshpower-transparent.png" width="auto">
  </a>
</h1>

<h1 align="center"> A powerful theme for ZSH </h1>

[![Tests](https://github.com/snakypy/zshpower/workflows/Tests/badge.svg)](https://github.com/snakypy/zshpower/actions)
[![Python Versions](https://img.shields.io/pypi/pyversions/zshpower)](https://pyup.io/repos/github/snakypy/zshpower/)
[![Updates](https://pyup.io/repos/github/snakypy/zshpower/shield.svg)](https://pyup.io/repos/github/snakypy/zshpower/)
[![Python Whell](https://img.shields.io/pypi/wheel/zshpower)](https://pypi.org/project/wheel/)
[![PyPI](https://img.shields.io/pypi/v/zshpower)](https://pypi.org/project/zshpower/#history)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/zshpower)](https://pypi.org/project/zshpower)
[![Isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/zshpower)](https://pypi.org/project/zshpower/#files)
[![GitHub license](https://img.shields.io/github/license/snakypy/zshpower)](https://github.com/snakypy/zshpower/blob/master/LICENSE)

----------------

<div align="center">
  <h4>
    | <a href="#features">Features</a> |
    <a href="#requirements">Requirements</a> |
		<a href="#pre-install">Pre-Install</a> |
    <a href="#installing">Install</a> |
    <a href="#post-install">Post-Install</a> |
    <a href="#theme-configuration">Theme configuration</a> |
    <a href="#reset-settings">Reset settings</a> |
    <a href="#upgrading">Upgrade</a> |
    <a href="#syncronize">Syncronize</a> |
    <a href="#deactivate-and-activate-theme-for-oh-my-zsh">Deactivate/Activate for Oh My ZSH</a> |
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

**ZSHPower** is a theme for [ZSH](https://www.zsh.org/); especially for the developer of various programming languages and [Linux](https://www.kernel.org/) users. Pleasant to look at, the **ZSHPower** comforts you with its vibrant colors and icons.

Installing **ZSHPower** is the easiest thing you will see in any existing theme for **ZSH**, because there is a manager.

The changes in the theme become more dynamic through a configuration file, where the user can make various combinations for the style of **ZSHPower**.

The **ZSHPower** supports installation along with [Oh My ZSH](https://ohmyz.sh/), where changes to: **enable** and **disable** an [Oh My ZSH](https://ohmyz.sh/) theme are easier, all in a simplified command line, without opening any files or creating symbolic links.

In addition, the **ZSHPower** manager downloads **Oh My Zsh** and the
[`zsh-autosuggestions`](https://github.com/zsh-users/zsh-autosuggestions) and [`zsh-syntax-highlighting`](https://github.com/zsh-users/zsh-syntax-highlighting) plugins automatically, everything to make your ZSH very power.

<div align="center">
	<sub><strong>Note:</strong> While this project is in beta, it will present some difficulties in terms of performance. Currently a prototype.</sub>
</div>

<br>
<br>

Here is an example of the installed **ZSHPower**:

<p align="center">
  <img alt="ZSHPower in Terminator" src="https://raw.githubusercontent.com/snakypy/assets/master/zshpower/demo/gifs/example-zshpower.gif" width="980px">
</p>

## Contributions

[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/0)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/0)[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/1)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/1)[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/2)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/2)[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/3)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/3)[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/4)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/4)[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/5)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/5)[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/6)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/6)[![](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/images/7)](https://sourcerer.io/fame/williamcanin/snakypy/zshpower/links/7)

## Features

- [Oh My Zsh](https://ohmyz.sh) installation automatically;*

- Automatically install [`zsh-autosuggestions`](https://github.com/zsh-users/zsh-autosuggestions) and [`zsh-syntax-highlighting`](https://github.com/zsh-users/zsh-syntax-highlighting);*

- Automated installation and uninstallation;

- Enable and disable `ZSHPower` anytime;*

- Open configuration file in the terminal itself;

- Reset the settings with one command only;

- Personalized directory with truncate option;

- Current Git branch and rich repo status;
  - untracked changes;
  - new files added;
  - deleted files;
  - new modified files;
  - commits made;
  - and more.

- Application versions shown with [icons](https://www.nerdfonts.com), they are:

  > .NET, C, C++, CMake, Crystal, Dart, Deno, Docker, Elixir, Ember, Erlang, Go, Gulp, Helm, Java, Julia, Kotlin,
  >
  > Lua, Nim, NodeJS (Javascript), OCaml, Perl, Php, Python, Ruby, Rust, Scala, V, Vagrant, Zig

- Package versions such as Crystal, Helm, NodeJS, Python, Rust shown;

- Shows the time in the upper right corner;

- and, many other dynamic settings in ```$HOME/.zshpower/config/zshpower.toml```.

**features if used with __Oh My ZSH__.*

## Requirements

To work correctly, you will first need:

- [`Git`](https://git-scm.com/downloads) (v2.25 or recent) must be installed;
- [`Zsh`](http://www.zsh.org/) (v5.2 or recent) must be installed;
- [`Python`](https://python.org) (v3.9 or recent);
- [`Sqlite3`](https://www.sqlite.org) (v3.35 or recent);
- [`Pip`](https://pip.pypa.io/en/stable/) (v21.0.1 or recent) must be installed;
- Some [`Nerd Font`](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/) font installed;
- One of that editor [vim](https://www.vim.org/), [nano](https://www.nano-editor.org/) or [emacs](https://www.gnu.org/software/emacs/) must be installed;


## Pre install

1 - Install the required packages in your distribution:

**Arch Linux and derivatives**
```shell
sudo pacman -S zsh vim curl git sqlite python python-pip
````

**Debian and derivatives**
```shell
sudo apt update
sudo apt install zsh vim curl git sqlite3 python3 python3-pip python3-venv
```

**Fedora and derivatives**
```shell
sudo dnf update
sudo dnf install zsh vim curl git sqlite python3 python3-pip util-linux-user
```

2 - Adding user's bin path to PATH:

```shell
export PATH="$PATH:$HOME/.local/bin"
```

2.1 - Switch from **Bash** to **Zsh** and export PATH's (**Optional**):

```shell
sudo chsh -s /usr/bin/zsh $(whoami)
exec zsh
export PATH="$PATH:$HOME/.local/bin"
```
> Note: By default, `ZSHPower` already performs this step at configuration time.

## Installing

**1** - It's time to install `ZSHPower` manager. To do this, do:

> NOTE: Global installation is not recommended. The easiest and most convenient way to use **ZSHPower** is to install for each different user on the machine, including for the super user (root)

```shell
$ python3 -m pip install zshpower --user -U
```

> NOTE: If you are installing to the user's local environment, be sure to add the environment variables to the `zshrc` file.


**2** - After installing **ZSHPower**, you need to generate the configuration files, how you will use **ZSHPower**. You basically have two ways to use **ZSHPower**. The first is to use independently, and the second is to use with **Oh My ZSH**.

To use independently, without any framework, do:

```shell
$ zshpower init
```

> **NOTE**:  This option you will have to add the following code to the `.zshrc` file.

> `eval $(zshpower init --path)`

If you want to use it with **Oh My ZSH** and, to make **ZSHPower** more powerfull, do:

```shell
$ zshpower init --omz
```

## Post-Install

The `ZSHPower` project uses the ["Nerd Font"](https://www.nerdfonts.com/font-downloads). You must install any of these fonts to terminally recognize the symbols.

However, by default, `ZSHPower` already downloads the font [**DejaVuSansMono Nerd Font**](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/DejaVuSansMono) in the folder (`$HOME/.fonts`) of user fonts using **Linux** system.

### Editors, IDE and Terminal

After install `ZSHPower` and the `DejaVuSansMono Nerd Font`, you must configure your text editor and terminal to recognize the icons used by the `Snakypy Prompt`.

**Visual Studio Code:**

Add the font family in [`Visual Studio Code`](https://code.visualstudio.com/),
opening the global settings for `Visual Studio Code` and add this information:

```json
{
	"terminal.integrated.fontFamily": "'<Your main source>', 'DejaVuSansMono Nerd Font'"
}
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

The configuration file is found in **$HOME/.zshpower/config/zshpower.toml**.

By default, most settings are set to **false**.

The **ZSHPower** configuration file is very intuitive, and just a glance gives you an idea of what each option does. But even so, note some of the main keys:

* **color.enable** - If `true`, enable the colors, otherwise `false` enters negative mode. `Default:` *true*

* **jump_line.enable** - If this option is `true`, you will skip a line each time you execute a command. `Default:` *true*

* **separator.element** - Add separators to each information shown by ZSHPower. `Default:` *-*

* **config.editor** - Choose of terminal editor that will open the configuration file. `Default:` *vim*

* **separator.color** - Changes the color of the separator. `Default:` *negative*

* **position** -  This option changes the position of certain sections. To show the information for a given tool, it must be listed in **position**.

* **enable** - If it is "true", it will activate the functionality where the "enable" key is.

* **symbol** - Must receive an icon, whether in unicode or not.

* **color** - Change the color of a particular block. Supported colors are: `black|white|blue|red|cyan|magenta|green|yellow`

* **color.symbol** - Option to change the color of the informed symbol.

* **prefix.color** - Changes the prefix color before the object shown.

* **prefix.text** - Before showing the object, show a prefix. You can put any text you like.

* **truncation_length** - This option receives an integer from 0 to 4. You will be responsible for truncating the path levels of the directory. `Default:` *1* (Note: Value 0 (zero), show all path.)

* **branch.color** - Option to change the color of the informed branch.

* **symbols.enable** -  Receives `true` or `false`. If `true`, shows the git status icons through each defined value. Remember that these icons will not be shown if you are via SSH. `Default:` *true*

* **new_line.enable** - Receive `true` or` false`. If `true`, skip a line in the command entry. `Default:` *true*

* **error.symbol** - Shows a symbol if the command output is false. `Default:` *\uf553*

* **error.color** - Error exit symbol color. `Default:` *red*

* **display** - A list of programming languages that support packaging. If you don't want the version of a package for a specific programming language to appear, just remove it from this list. `Default:` ["python", "node", "rust", "scala", "crystal", "helm"]

* **version.enable** - If `true`, show version information for a particular tool.  `Default:` *false*

* **version.micro.enable** - If `true`, show the micro version information of a given tool. Note: The `version.enable` key must be` true`. `Default:` *true*

* **involved** - Element that will enclose the name of an object. By default you should be given two unique elements. `Default:` []

* **normal.enable** - If the option is `true`, it will show the real name of the virtual machine. If the option is `false`, the user has the possibility to enter text. `Default:` true

* **py.enable** - Shows the version of python on behalf of the virtual machine. `Default:` *true*

* **hash.enable** - Displays the hash of the virtual machine name if it was created using [Poetry](https://python-poetry.org/). `Default:` *true*

* **seconds.enable** - Receive `true` or` false`. If it has `true`, show the seconds of the clock. `Default:` false

* **show_greater_than** - It will only be shown if the return time of the command if it is greater than the value of this option.  `Default:` 1
                          > NOTE: It must be a value in seconds.


## Synchronize

`ZSHPower` stores some information in a database (SQLite 3) to obtain better performance and speed in the display of data. This data is currently the versions of the applications that `ZSHPower` shows on the console. Before, `ZSHPower` showed this information in real time, but it compromised performance and display time.

With that, every time you update the program you work on (or even the entire system), you need to synchronize. To synchronize you have two options, the first is manual and the other automatically using a task scheduler, such as [Cronie](https://github.com/cronie-crond/cronie/).

### Sync manually:

```shell
$ zshpower sync
```

If you always want manual synchronization, it would be interesting whenever you update the system or a particular package that `ZSHPower` supports, add the synchronization command as well. For example:


```shell
# Debian and derivatives
$ sudo apt upgrade && zshpower sync
# Arch Linux and derivatives
$ sudo pacman -Syu && zshpower sync
# Fedora and derivatives
$ sudo dnf update && zshpower sync
```

### Automatically sync:

> IMPORTANT: Only if you have root permission.

`ZSHPower` has an option to create the task for database synchronization. This option is via the command:

```shell
zshpower cron --create
```

With this command, a `ZSHPower` task will be created in **Cron**, however you need to have **Cron** installed and have superuser (root) permission to perform the task creation, otherwise, nothing will happen.

By default, the task is created with comment, and you will have to set the values. For this, **ZSHPower** provides a command to open the **Cron** task file, with the command:

```shell
zshpower cron --open
```

As stated before, you can use a task scheduler. Just access **Cron** to schedule a task at any time and call this script. You can use the [Crontab Guru](https://crontab.guru/) website  to make it easier to understand Cron.

You can get more information about **Cron** through sample sites like these:

* https://crontab-generator.org/
* https://crontab.guru/crontab.5.html
* https://wiki.archlinux.org/title/Cron

or use the Crontab main:

```shell
$ man crontab
```
**An example using the [Cronie](https://github.com/cronie-crond/cronie) scheduling synchronization every 2 hours:**

Create or changing a file  (with superuser)`/etc/cron.d/zshpower` and put the following line

```shell
# ZSHPower Task - BEGIN
SHELL=/bin/zsh
PATH=/home/<USER>/.local/bin:/bin:/usr/local/bin:$PATH
export PATH
# Every 2 hours
0 */2 * * * <USER> zshpower sync
# ZSHPower Task - END
```

> In <USER> put the logged in user on the machine.

## Upgrading

If `ZSHPower` has any new features, please update the command line below:

```shell
$ python3 -m pip install zshpower --user -U
$ zshpower init [--omz]
```

## Reset settings

If you made any changes to the configuration file and regretted it, you can reset everything with the command below:

```shell
$ zshpower reset --config
```

You can also reset the **ZSHPower** database if it is corrupted with the command below:

```shell
$ zshpower reset --db
```

## Deactivate and Activate theme for Oh My ZSH

You can activate and deactivate **ZSHPower** at any time, without opening any files, if using with Oh My ZH. To do this, follow the steps below:

* Deactivate

```shell
$ zshpower deactivate
```

When deactivate, the manager will return to the default [Oh My Zsh](https://github.com/robbyrussell/oh-my-zsh#selecting-a-theme) theme, the `robbyrussell`.
If you want to deactivate with another theme already installed, use the `--theme` option. Example:

```shell
$ zshpower deactivate --theme=agnoster
```

* Activate

```shell
$ zshpower activate
```

## Uninstalling

We will be sad if you want to stop using **ZSHPower**, but for an easier and more effective uninstall, we also have the command:

```shell
$ zshpower uninstall
```

> NOTE: If you installed "**ZSHPower**" with 'sudo', use 'sudo' to uninstall as well.

```shell
$ sudo zshpower uninstall
```

## More Commands

For more command information, use:

```shell
$ zshpower --help
```

## Donation

Click on the image below to be redirected the donation forms:

<div class="donate">
  <a href="https://github.com/snakypy/donations/blob/main/README.md">
    <img width="160" height="100" src="https://raw.githubusercontent.com/snakypy/donations/main/svg/donate/donate-hand.svg" alt="Donations">
  </a>
</div>

## License

The project is available as open source under the terms of the [MIT License](https://github.com/snakypy/zshpower/blob/main/LICENSE) ©

## Credits

See, [AUTHORS](https://github.com/snakypy/zshpower/blob/main/AUTHORS.rst).
