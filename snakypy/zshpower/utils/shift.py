from getpass import getpass
from os import remove, walk
from os.path import exists, isdir, isfile, join
from re import M as re_m
from re import sub as re_sub
from shutil import rmtree, which
from subprocess import PIPE, Popen, check_output
from sys import platform
from zipfile import ZipFile

from snakypy.helpers import FG, printer
from snakypy.helpers.files import backup_file, create_file
from snakypy.helpers.path import create as snakypy_path_create
from snakypy.helpers.subprocess import command
from tomlkit import dumps as toml_dumps
from tomlkit import parse as toml_parse

from snakypy.zshpower import __info__
from snakypy.zshpower.utils.catch import (
    plugins_current_zshrc,
    read_zshrc,
    read_zshrc_omz,
)


def create_config(content, file_path, *, force=False) -> bool:
    if not exists(file_path) or force:
        parsed_toml = toml_parse(content)
        write_toml = toml_dumps(parsed_toml)
        create_file(write_toml, file_path, force=force)
        return True
    return False


def create_zshrc(content, zshrc) -> bool:
    if exists(zshrc):
        if not read_zshrc_omz(zshrc):
            backup_file(zshrc, zshrc, date=True, extension=False)
            create_file(content, zshrc, force=True)
            return True
    elif not exists(zshrc):
        create_file(content, zshrc)
        return True
    return False


def cron_task(sync_context, sync_path, cron_context, cron_path):

    if not exists(sync_path) or not exists(cron_path):
        pass_ok = False

        message = """
                At this point, you need to INFORM the root password to create the Crontab task.
                If you do not want this configuration to be made, you can cancel with Ctrl + C.
                """

        printer(message, foreground=FG().WARNING)

        while not pass_ok:
            sudo_password = getpass()

            command_ = f"""su -c 'echo "{sync_context}" > {sync_path}; chmod a+x {sync_path};
            echo "{cron_context}" > {cron_path};'
            """
            p = Popen(
                command_,
                stdin=PIPE,
                stderr=PIPE,
                stdout=PIPE,
                universal_newlines=True,
                shell=True,
            )
            communicate = p.communicate(sudo_password)

            if "failure" in communicate[1].split():
                printer("Password incorrect.", foreground=FG().ERROR)
            else:
                pass_ok = True


def change_theme_in_zshrc(zshrc, theme_name) -> bool:
    if read_zshrc_omz(zshrc):
        current_zshrc = read_zshrc(zshrc)
        current_theme = read_zshrc_omz(zshrc)[1]
        new_theme = f'ZSH_THEME="{theme_name}"'
        new_zsh_rc = re_sub(rf"{current_theme}", new_theme, current_zshrc, flags=re_m)
        create_file(new_zsh_rc, zshrc, force=True)
        return True
    return False


def omz_install(omz_root):
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
        raise Exception("Error downloading Oh My ZSH. Aborted!")


def omz_install_plugins(omz_root, plugins):
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
        raise Exception("There was an error installing the plugin")


def install_fonts(home, *, force=False) -> bool:
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

    new_plugins = [plugin for plugin in plugins if plugin not in current]

    if len(new_plugins) > 0:
        current_zshrc = read_zshrc(zshrc)
        plugins = f'plugins=({" ".join(current)} {" ".join(new_plugins)})'
        new_zsh_rc = re_sub(r"^plugins=\(.*", plugins, current_zshrc, flags=re_m)
        create_file(new_zsh_rc, zshrc, force=True)
        return new_zsh_rc
    return ""


def rm_source_zshrc(zshrc):
    current_zshrc = read_zshrc(zshrc)
    line_rm = f"source\\ \\$HOME/.zshpower/{__info__['version']}/init.sh"
    new_zshrc = re_sub(rf"{line_rm}", "", current_zshrc, flags=re_m)
    create_file(new_zshrc, zshrc, force=True)


def uninstall_by_pip(*, packages=()) -> tuple:
    if which("pip") is not None:
        for pkg in packages:
            check_output(
                f"pip uninstall {pkg} -y",
                shell=True,
                universal_newlines=True,
            )
    return packages


def remove_versions_garbage(path) -> None:
    folders = []
    for root, dirs, files in walk(path):
        for item in dirs:
            folders.append(item)

    for folder in folders:
        if join(path, folder) != join(path, __info__["version"]):
            rmtree(join(path, folder), ignore_errors=True)
