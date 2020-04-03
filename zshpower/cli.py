"""CLI - Command Line Interface"""
import snakypy
from snakypy import FG
from zshpower import decorators, utils
from zshpower import HOME, __pkginfo__, __version__
from zshpower.zshpower import ZSHPower

zp = ZSHPower(HOME)


@decorators.assign_cli(zp.arguments(), "init")
def init():
    zp.init_command(reload=True, message=True)


@decorators.assign_cli(zp.arguments(), "config")
def config_action():
    zp.config_command()


@decorators.assign_cli(zp.arguments(), "activate")
def activate():
    zp.activate_command()


@decorators.assign_cli(zp.arguments(), "deactivate")
def deactivate():
    zp.deactivate_command()


@decorators.assign_cli(zp.arguments(), "reset")
def reset_config():
    zp.reset_command()


@decorators.assign_cli(zp.arguments(), "uninstall")
def uninstall():
    zp.uninstall_command()


@decorators.assign_cli(zp.arguments(), "--credits")
def credence():
    utils.show_billboard()
    snakypy.console.credence(
        __pkginfo__["name"],
        __version__,
        __pkginfo__["home_page"],
        __pkginfo__,
        foreground=FG.CYAN,
    )


def main():
    init()
    config_action()
    activate()
    deactivate()
    reset_config()
    uninstall()
    credence()
