from getpass import getpass
from os import remove
from os.path import exists, isdir, isfile, join
from re import M, sub
from shutil import which
from subprocess import PIPE, Popen, check_output
from sys import exit, platform
from zipfile import ZipFile

from snakypy.helpers import FG, printer
from snakypy.helpers.files import backup_file, create_file
from snakypy.helpers.logging import Log
from snakypy.helpers.path import create as create_path
from snakypy.helpers.subprocess import command
from tomlkit import dumps as toml_dumps
from tomlkit import parse as toml_parse

from snakypy.zshpower.utils.catch import current_plugins, get_zsh_theme, read_file_log


def create_toml(content, file, *, force=False) -> bool:
    """
    Create the ZSHPower configuration file. A TOML file.
    """
    if not exists(file) or force:
        parsed_toml = toml_parse(content)
        write_toml = toml_dumps(parsed_toml)
        create_file(write_toml, file, force=force)
        return True
    return False


def create_zshrc(content, zshrc_path, logfile):
    """
    Create a .zshrc file if there is no one compatible with Oh MyZSH.
    """
    try:
        if not get_zsh_theme(zshrc_path, logfile):
            backup_file(zshrc_path, zshrc_path, date=True, extension=False)
            create_file(content, zshrc_path, force=True)
    except FileNotFoundError:
        create_file(content, zshrc_path)


def command_root(cmd, logfile=None, msg_header="Enter the machine root password"):
    check = False
    printer(f"[ {msg_header} ]", foreground=FG().WARNING)
    try:
        while not check:
            sudo_password = getpass()
            popen = Popen(
                cmd,
                stdin=PIPE,
                stderr=PIPE,
                stdout=PIPE,
                universal_newlines=True,
                shell=True,
            )
            communicate = popen.communicate(sudo_password)
            if "su:" in communicate[1].split():
                printer("Password incorrect.", foreground=FG().ERROR)
            else:
                check = True
        return check
    except KeyboardInterrupt:
        printer("Aborted by user.", foreground=FG().WARNING)
        exit()
    except PermissionError:
        if logfile:
            Log(filename=logfile).record(
                "No permission to write to directory.", colorize=True, level="error"
            )
        raise PermissionError("No permission to write to directory")


def change_theme(file, theme_name, logfile) -> bool:
    """
    Change Oh My ZSH Theme
    """
    if get_zsh_theme(file, logfile):
        current_file = read_file_log(file, logfile)
        current_theme = get_zsh_theme(file, logfile)[1]
        new_theme = f'ZSH_THEME="{theme_name}"'
        new_file = sub(rf"{current_theme}", new_theme, current_file, flags=M)
        create_file(new_file, file, force=True)
        return True
    return False


def omz_install(omz_root, logfile):
    """
    Install Oh My ZSH
    """
    omz_github = "https://github.com/ohmyzsh/ohmyzsh.git"
    cmd_line = f"git clone {omz_github} {omz_root}"
    try:
        if not exists(omz_root):
            printer("Install Oh My ZSH...", foreground=FG().QUESTION)
            command(cmd_line, verbose=True)
            printer(
                "Oh My ZSH installation process finished.",
                foreground=FG().FINISH,
            )

    except Exception:
        Log(filename=logfile).record(
            "Error downloading Oh My ZSH. Aborted!", colorize=True, level="error"
        )
        raise Exception("Error downloading Oh My ZSH. Aborted!")


def install_plugins(omz_root, plugins, logfile):
    """
    Install plugins on Oh My ZSH
    """
    try:
        url_master = "https://github.com/zsh-users"
        for plugin in plugins:
            path = join(omz_root, f"custom/plugins/{plugin}")
            clone = f"git clone {url_master}/{plugin}.git {path}"
            if not isdir(path):
                printer(f"Install plugins {plugin}...", foreground=FG().QUESTION)
                command(clone, verbose=True)
                printer(f"Plugin {plugin} task finished!", foreground=FG().FINISH)
    except Exception:
        Log(filename=logfile).record(
            "There was an error installing the plugin", colorize=True, level="error"
        )
        raise Exception("There was an error installing the plugin")


def install_fonts(home, logfile, *, force=False) -> bool:
    """
    Install the Nerd Fonts font in the $HOME/.fonts folder
    """
    url = "https://github.com/snakypy/assets"
    base_url = "raw/main/zshpower/fonts/terminal/fonts.zip"
    font_name = "DejaVu Sans Mono Nerd Font"
    fonts_dir = join(home, ".fonts")
    create_path(fonts_dir)
    curl_output = join(home, "zshpower__font.zip")

    if platform.startswith("linux"):
        try:
            if (
                not isfile(join(fonts_dir, "DejaVu Sans Mono Nerd Font Complete.ttf"))
                or force
            ):
                printer(
                    f'Please wait, downloading the "{font_name}" font and'
                    "installing...",
                    foreground=FG().QUESTION,
                )
                cmd_line = f"curl -L {join(url, base_url)} -o {curl_output}"
                command(cmd_line, verbose=True)

                with ZipFile(curl_output, "r") as zip_ref:
                    zip_ref.extractall(fonts_dir)
                    remove(curl_output)
                    printer("Done!", foreground=FG().FINISH)
                return True
            return False
        except Exception as err:
            Log(filename=logfile).record(
                f'Error downloading font "{font_name}"', colorize=True, level="error"
            )
            raise Exception(f'Error downloading font "{font_name}"', err)
    return False


def add_plugins(zshrc, logfile):
    """
    Add plugins to the .zshrc file if it is compatible with Oh My ZSH
    """
    plugins = (
        "python",
        "pip",
        "pep8",
        "autopep8",
        "virtualenv",
        "zsh-syntax-highlighting",
        "zsh-autosuggestions",
    )
    current = current_plugins(zshrc, logfile)

    new_plugins = [plugin for plugin in plugins if plugin not in current]

    if len(new_plugins) > 0:
        current_zshrc = read_file_log(zshrc, logfile)
        plugins = f'plugins=({" ".join(current)} {" ".join(new_plugins)})'
        new_zsh_rc = sub(r"^plugins=\(.*", plugins, current_zshrc, flags=M)
        create_file(new_zsh_rc, zshrc, force=True)
        return new_zsh_rc
    return ""


def remove_lines(file, logfile, lines=()) -> None:
    """
    Remove certain lines from a file
    """
    content = read_file_log(file, logfile)
    for num, _ in enumerate(lines):
        content = sub(rf"{lines[num]}", "", content, flags=M)

    create_file(content, file, force=True)


def pip_uninstall(*, packages=()) -> tuple:
    """
    Install Python packages for active user using Pip
    """
    if which("pip") is not None:
        for pkg in packages:
            check_output(
                f"pip uninstall {pkg} -y",
                shell=True,
                universal_newlines=True,
            )
    return packages
