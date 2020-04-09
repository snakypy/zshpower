from snakypy.ansi import FG, NONE
from zshpower.config import package

robbyrussell = f"{FG.MAGENTA}robbyrussell{NONE}"

options = f"""
{FG.MAGENTA}Welcome to the {package.info["pkg_name"]} options menu.{NONE}

Usage:
    {package.info['executable']} init
    {package.info['executable']} config (--open | --view)
    {package.info['executable']} activate
    {package.info['executable']} deactivate [--theme=<name>]
    {package.info['executable']} reset
    {package.info['executable']} uninstall
    {package.info['executable']} --help
    {package.info['executable']} --version
    {package.info['executable']} --credits

Arguments:
    {FG.CYAN}init{NONE} ---------- Install dependencies like Oh My ZSH and plugins and activate the
                    {package.info["name"]} theme.
    {FG.CYAN}activate{NONE} ------ Activate the {package.info["name"]} theme.
    {FG.CYAN}deactivate{NONE} ---- Deactivate the {package.info["name"]} theme and go back to the default.
    {FG.CYAN}reset{NONE} --------- Reset to default settings.
    {FG.CYAN}uninstall{NONE} ----- Uninstall the package {package.info["name"]}.
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
