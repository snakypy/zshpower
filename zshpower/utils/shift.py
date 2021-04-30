from getpass import getpass
from subprocess import Popen, PIPE
from tomlkit import dumps as toml_dumps
from tomlkit import parse as toml_parse
from os.path import isdir
from shutil import copyfile as shutil_copyfile
from datetime import datetime
from snakypy.console import cmd as cmd_snakypy
from snakypy.file import create as snakypy_file_create
from re import sub as re_sub, M as re_m
from os.path import join, exists
from snakypy import printer, FG
from zshpower.utils.catch import read_zshrc_omz, read_zshrc
from sys import platform
from os.path import isfile
from zipfile import ZipFile
from os import remove as os_remove
from snakypy.path import create as snakypy_path_create
from zshpower.utils.catch import plugins_current_zshrc


def create_config(content, file_path, force=False):
    if not exists(file_path) or force:
        parsed_toml = toml_parse(content)
        write_toml = toml_dumps(parsed_toml)
        snakypy_file_create(write_toml, file_path, force=force)
        return True
    return False


def create_zshrc(content, zshrc):
    if exists(zshrc):
        if not read_zshrc_omz(zshrc):
            shutil_copyfile(zshrc, f"{zshrc}-{datetime.today().isoformat()}")
            snakypy_file_create(content, zshrc, force=True)
            return True
    elif not exists(zshrc):
        snakypy_file_create(content, zshrc)
        return True
    return False


def create_zshrc_not_exists(content, zshrc):
    if not exists(zshrc):
        snakypy_file_create(content, zshrc)


def create_file_superuser(context=(), filepath=()):

    pass_ok = False

    message = """
            At this point, you need to INFORM the root password to create the Crontab task.
            If you do not want this configuration to be made, you can cancel with Ctrl + C.
            """

    printer(message, foreground=FG.WARNING)

    while not pass_ok:

        sudo_password = getpass()

        communicate = ()
        for context_ in context:
            for filepath_ in filepath:

                command = f"""su -c 'echo "{context_}" > {filepath_}; chmod a+x {filepath_}'"""

                p = Popen(
                    command,
                    stdin=PIPE,
                    stderr=PIPE,
                    stdout=PIPE,
                    universal_newlines=True,
                    shell=True,
                )

                communicate = p.communicate(sudo_password)

        if "failure" in communicate[1].split():
            printer("Password incorrect.", foreground=FG.ERROR)
        else:
            pass_ok = True


def change_theme_in_zshrc(zshrc, theme_name):
    if read_zshrc_omz(zshrc):
        current_zshrc = read_zshrc(zshrc)
        current_theme = read_zshrc_omz(zshrc)[1]
        new_theme = f'ZSH_THEME="{theme_name}"'
        new_zsh_rc = re_sub(rf"{current_theme}", new_theme, current_zshrc, flags=re_m)
        snakypy_file_create(new_zsh_rc, zshrc, force=True)
        return True
    return False


def omz_install(omz_root):
    omz_github = "https://github.com/ohmyzsh/ohmyzsh.git"
    cmd_line = f"git clone {omz_github} {omz_root}"
    try:
        if not exists(omz_root):
            printer("Install Oh My ZSH...", foreground=FG.QUESTION)
            cmd_snakypy(cmd_line, verbose=True)
            printer(
                "Oh My ZSH installation process finished.",
                foreground=FG.FINISH,
            )

    except Exception:
        raise Exception("Error downloading Oh My ZSH. Aborted!")


def omz_install_plugins(omz_root, plugins):
    try:
        url_master = "https://github.com/zsh-users"
        for plugin in plugins:
            path = join(omz_root, f"custom/plugins/{plugin}")
            clone = f"git clone {url_master}/{plugin}.git {path}"
            if not isdir(path):
                printer(f"Install plugins {plugin}...", foreground=FG.QUESTION)
                cmd_snakypy(clone, verbose=True)
                printer(f"Plugin {plugin} task finished!", foreground=FG.FINISH)
    except Exception:
        raise Exception("There was an error installing the plugin")


def install_fonts(home, force=False):
    url = "https://github.com/snakypy/snakypy-static"
    base_url = "blob/master/zshpower/fonts/fonts.zip?raw=true"
    font_name = "DejaVu Sans Mono Nerd Font"
    fonts_dir = join(home, ".fonts")
    snakypy_path_create(fonts_dir)
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
                    foreground=FG.QUESTION,
                )
                cmd_line = f"curl -L {join(url, base_url)} -o {curl_output}"
                cmd_snakypy(cmd_line, verbose=True)

                with ZipFile(curl_output, "r") as zip_ref:
                    zip_ref.extractall(fonts_dir)
                    os_remove(curl_output)
                    printer("Done!", foreground=FG.FINISH)
                return True
            return False
        except Exception as err:
            raise Exception(f'Error downloading font "{font_name}"', err)
    return False


def add_plugins_zshrc(zshrc):
    plugins = (
        "python",
        "django",
        "pip",
        "pep8",
        "autopep8",
        "zsh-syntax-highlighting",
        "zsh-autosuggestions",
    )
    current = plugins_current_zshrc(zshrc)

    # TODO: No List Comprehension (DEPRECATED)
    # new_plugins = []
    # for plugin in plugins:
    #     if plugin not in current:
    #         new_plugins.append(plugin)

    new_plugins = [plugin for plugin in plugins if plugin not in current]

    if len(new_plugins) > 0:
        current_zshrc = read_zshrc(zshrc)
        plugins = f'plugins=({" ".join(current)} {" ".join(new_plugins)})'
        new_zsh_rc = re_sub(r"^plugins=\(.*", plugins, current_zshrc, flags=re_m)
        snakypy_file_create(new_zsh_rc, zshrc, force=True)
        return new_zsh_rc
    return


def rm_source_zshrc(zshrc):
    current_zshrc = read_zshrc(zshrc)
    line_rm = "source\\ \\$HOME/.zshpower"
    new_zshrc = re_sub(rf"{line_rm}", "", current_zshrc, flags=re_m)
    snakypy_file_create(new_zshrc, zshrc, force=True)
