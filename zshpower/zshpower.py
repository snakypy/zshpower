"""Main module."""
import os
import shutil
import contextlib
import pydoc
import subprocess
import snakypy
from sys import exit
from textwrap import dedent
from datetime import datetime
from zshpower import __version__, __pkginfo__
from zshpower import utils, config
from snakypy import printer, FG, pick
from docopt import docopt
from snakypy.ansi import NONE
from os.path import join


class ZSHPower:
    def __init__(self, home):
        self.HOME = home
        self.config_root = join(self.HOME, f".config/snakypy/zshpower/{__version__}")
        self.config = join(self.config_root, "config.toml")
        self.zsh_rc = join(self.HOME, ".zshrc")
        self.omz_root = join(self.HOME, ".oh-my-zsh")
        self.themes_folder = join(self.omz_root, "custom/themes")
        self.theme_file = join(
            self.themes_folder, f"{__pkginfo__['pkg_name']}.zsh-theme"
        )
        self.plugins = ("zsh-syntax-highlighting", "zsh-autosuggestions")
        robbyrussell = f"{FG.MAGENTA}robbyrussell{NONE}"
        self.menu_opts = dedent(
            f"""
        {FG.MAGENTA}Welcome to the {__pkginfo__["pkg_name"]} options menu.{NONE}

        Usage:
            {__pkginfo__['executable']} init
            {__pkginfo__['executable']} config (--open | --view)
            {__pkginfo__['executable']} activate
            {__pkginfo__['executable']} deactivate [--theme=<name>]
            {__pkginfo__['executable']} reset
            {__pkginfo__['executable']} uninstall
            {__pkginfo__['executable']} --help
            {__pkginfo__['executable']} --version
            {__pkginfo__['executable']} --credits

        Arguments:
            {FG.CYAN}init{NONE} ---------- Install dependencies like Oh My ZSH and plugins and activate the
                            {__pkginfo__["name"]} theme.
            {FG.CYAN}activate{NONE} ------ Activate the {__pkginfo__["name"]} theme.
            {FG.CYAN}deactivate{NONE} ---- Deactivate the {__pkginfo__["name"]} theme and go back to the default.
            {FG.CYAN}reset{NONE} --------- Reset to default settings.
            {FG.CYAN}uninstall{NONE} ----- Uninstall the package {__pkginfo__["name"]}.
            {FG.CYAN}config{NONE} -------- The easiest way to edit and view the settings is through this option.

        Options:
            {FG.CYAN}--help{NONE} --------- Show this screen.
            {FG.CYAN}--open{NONE} --------- Open the configuration file in edit mode and perform the automatic update
                             when you exit.
            {FG.CYAN}--view{NONE} --------- View the configuration file on the terminal.
            {FG.CYAN}--theme=<name>{NONE} - Get the name of a theme available on Oh My ZSH [Default: {robbyrussell}].
            {FG.CYAN}--version{NONE} ------ Show version.
            {FG.CYAN}--credits{NONE} ------ Show credits.
                """
        )

    def arguments(self, argv=None):
        formatted_version = (
            f"{__pkginfo__['name']} version: {FG.CYAN}{__version__}{NONE}"
        )
        data = docopt(self.menu_opts, argv=argv, version=formatted_version)
        return data

    def init_command(self, reload=False, message=False):
        utils.tools_requirements("git", "vim", "zsh")
        snakypy.path.create(self.config_root)
        utils.create_config(config.config_content(), self.config)
        utils.omz_install(self.omz_root)
        utils.omz_install_plugins(self.omz_root, self.plugins)
        utils.install_fonts()
        utils.create_zshrc(config.zshrc_content(self.omz_root), self.zsh_rc)
        utils.change_theme_in_zshrc(self.zsh_rc, "zshpower")
        utils.add_plugins_zshrc(self.zsh_rc)
        snakypy.file.create(config.theme_content(), self.theme_file, force=True)
        utils.change_shell()
        printer("Done!", foreground=FG.FINISH) if message else None
        utils.reload_zsh() if reload else None

    def config_command(self):
        utils.checking_init(self.themes_folder)

        if self.arguments()["--open"]:
            editors = ("vim", "nano", "emacs")
            for editor in editors:
                if shutil.which(editor):
                    get_editor = os.environ.get("EDITOR", editor)
                    with open(self.config) as f:
                        subprocess.call([get_editor, f.name])
                    return True
        elif self.arguments()["--view"]:
            read_config = snakypy.file.read(self.config)
            pydoc.pager(read_config)
            return True

    def activate_command(self):
        utils.checking_init(self.themes_folder)

        if utils.read_zshrc(self.zsh_rc)[0] == "zshpower":
            printer("Already activated. Nothing to do.", foreground=FG.GREEN)
            exit(0)
        utils.change_theme_in_zshrc(self.zsh_rc, "zshpower")
        printer("Activation process finish.", foreground=FG.FINISH)
        utils.reload_zsh()

    def deactivate_command(self, *, theme_name="robbyrussell"):
        utils.checking_init(self.themes_folder)

        if not utils.read_zshrc(self.zsh_rc)[0] == "zshpower":
            printer("Already disabled. Nothing to do.", foreground=FG.GREEN)
            exit(0)
        if not self.arguments()["--theme"]:
            utils.change_theme_in_zshrc(self.zsh_rc, theme_name)
        else:
            utils.change_theme_in_zshrc(self.zsh_rc, self.arguments()["--theme"])
        printer("Deactivation process finish.", foreground=FG.FINISH)
        utils.reload_zsh()

    def reset_command(self):
        utils.checking_init(self.themes_folder)
        utils.create_config(config.config_content(), self.config, force=True)
        printer("Reset process finished.", foreground=FG.FINISH)
        utils.reload_zsh()

    def uninstall_command(self):
        utils.checking_init(self.themes_folder)

        title = f"What did you want to uninstall?"
        options = [
            f"{__pkginfo__['name']}",
            f"{__pkginfo__['name']} and Oh My ZSH",
            "None",
        ]
        reply = pick(title, options, colorful=True, index=True)

        if reply is None or reply[0] == 2:
            printer("Whew! Thanks! :)", foreground=FG.GREEN)
            exit(0)

        with contextlib.suppress(Exception):
            os.remove(self.theme_file)

        pip_check = shutil.which("pip")
        if pip_check is not None:
            subprocess.check_output(
                f'pip uninstall {__pkginfo__["name"]} -y',
                shell=True,
                universal_newlines=True,
            )
        utils.change_theme_in_zshrc(self.zsh_rc, "robbyrussell")

        if reply[0] == 1:
            shutil.rmtree(self.omz_root, ignore_errors=True)
            with contextlib.suppress(Exception):
                shutil.copyfile(
                    self.zsh_rc, f"{self.zsh_rc}-D{datetime.today().isoformat()}"
                )
            with contextlib.suppress(Exception):
                os.remove(self.zsh_rc)

        utils.reload_zsh()

        printer("Uninstall process finished.", foreground=FG.FINISH)
