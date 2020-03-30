import snakypy
import os
import re
import shutil
import subprocess

try:
    import pwd
except ImportError:
    pass
import tomlkit
from os.path import join, exists, isdir, isfile
from datetime import datetime
from sys import platform
from snakypy import printer, FG
from zshpower import HOME, __pkginfo__
from zipfile import ZipFile


def show_billboard():
    """Function to create a billboard."""
    print("\n")
    printer("Offered by:".center(50), foreground=FG.GREEN)
    snakypy.console.billboard(
        __pkginfo__["organization_name"], justify="center", foreground=FG.YELLOW
    )
    printer(f"copyright (c) since 2020\n".center(100), foreground=FG.GREEN)


def tools_requirements(*args):
    for tool in args:
        if shutil.which(tool) is None:
            raise Exception(
                f'The package \'{__pkginfo__["name"]}\' needs the "{tool}" tool.'
                " Tool not found. Aborted."
            )


def checking_init(root):
    """Function that ends commands that depend on the created repository, but
    the repository was not created."""
    if not exists(join(root, f"{__pkginfo__['pkg_name']}.zsh-theme")):
        printer(
            f'Command "{__pkginfo__["pkg_name"]} init" has not been started.' "Aborted",
            foreground=FG.WARNING,
        )
        exit(1)
    return True


def create_config(content, file_path, force=False):
    if not exists(file_path) or force:
        parsed_toml = tomlkit.parse(content)
        write_toml = tomlkit.dumps(parsed_toml)
        snakypy.file.create(write_toml, file_path, force=force)
        return True
    return


def read_zshrc(zsh_rc):
    """ """
    if exists(zsh_rc):
        with open(zsh_rc) as r:
            content_ = r.read()
        m = re.search(r"ZSH_THEME=\".*", content_)
        if m is not None:
            zsh_theme = m.group(0)
            lst = zsh_theme.split("=")
            theme_name = [s.strip('"') for s in lst][1]
            return theme_name, content_, zsh_theme
    return False


def create_zshrc(content_, zsh_rc):
    if exists(zsh_rc):
        if not read_zshrc(zsh_rc):
            shutil.copyfile(zsh_rc, f"{zsh_rc}-D{datetime.today().isoformat()}")
            snakypy.file.create(content_, zsh_rc, force=True)
            return True
    elif not exists(zsh_rc):
        snakypy.file.create(content_, zsh_rc)
        return True
    return


def plugins_current_zshrc(zsh_rc):
    content_ = read_zshrc(zsh_rc)[1]
    m = re.search(r"^plugins=\(.*", content_, flags=re.M)
    if m is not None:
        get = m.group(0)
        lst = get.split("=")
        current = [i.strip('"').replace("(", "").replace(")", "") for i in lst][1]
        return current.split()


def add_plugins_zshrc(zsh_rc):
    plugins = (
        "python",
        "django",
        "pip",
        "pep8",
        "autopep8",
        "zsh-syntax-highlighting",
        "zsh-autosuggestions",
    )
    current = plugins_current_zshrc(zsh_rc)
    new_plugins = []
    for plugin in plugins:
        if plugin not in current:
            new_plugins.append(plugin)

    if len(new_plugins) > 0:
        plugins = f'plugins=({" ".join(current)} {" ".join(new_plugins)})'
        new_zsh_rc = re.sub(
            rf"^plugins=\(.*", plugins, read_zshrc(zsh_rc)[1], flags=re.M
        )
        snakypy.file.create(new_zsh_rc, zsh_rc, force=True)
        return new_zsh_rc
    return


def change_theme_in_zshrc(zsh_rc, theme_name):
    if read_zshrc(zsh_rc):
        current_theme = read_zshrc(zsh_rc)[2]
        new_theme = f'ZSH_THEME="{theme_name}"'
        new_zsh_rc = re.sub(
            rf"{current_theme}", new_theme, read_zshrc(zsh_rc)[1], flags=re.M
        )
        snakypy.file.create(new_zsh_rc, zsh_rc, force=True)
        return True
    return


def reload_zsh():
    subprocess.call("exec zsh", shell=True)


def bash_command(cmd):
    subprocess.Popen(["/bin/bash", "-c", cmd])


def current_shell():
    pw = pwd.getpwuid(os.getuid())
    path_shell = pw[-1]
    shell = str(path_shell).split("/")[-1]
    return shell, path_shell


def current_user():
    return str(os.popen("whoami").read()).replace("\n", "")


def change_shell():
    if current_shell()[0] != "zsh":
        try:
            subprocess.call(f"chsh -s $(which zsh) {current_user()}", shell=True)
        except KeyboardInterrupt:
            printer("Canceled by user", foreground=FG.WARNING)


def omz_install(omz_root):
    omz_github = "https://github.com/ohmyzsh/ohmyzsh.git"
    cmd_line = f"git clone {omz_github} {omz_root}"
    try:
        if not exists(omz_root):
            printer("Install Oh My ZSH...", foreground=FG.QUESTION)
            snakypy.console.cmd(cmd_line, verbose=True)
            printer(
                "Oh My ZSH installation process finished.", foreground=FG.FINISH,
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
                snakypy.console.cmd(clone, verbose=True)
                printer(f"Plugin {plugin} task finished!", foreground=FG.FINISH)
    except Exception:
        raise Exception(f"There was an error installing the plugin")


def install_fonts(force=False):
    url = "https://github.com/snakypy/snakypy-static"
    base_url = f"blob/master/zshpower/fonts/fonts.zip?raw=true"
    font_name = "DejaVu Sans Mono Nerd Font"
    fonts_dir = join(HOME, f".fonts")
    snakypy.path.create(fonts_dir)
    curl_output = join(HOME, "zshpower__font.zip")

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
                snakypy.console.cmd(cmd_line, verbose=True)

                with ZipFile(curl_output, "r") as zip_ref:
                    zip_ref.extractall(fonts_dir)
                    os.remove(curl_output)
                    printer("Done!", foreground=FG.FINISH)
                return True
            return
        except Exception as err:
            raise Exception(f'Error downloading font "{font_name}"', err)
    return
