from snakypy.ansi import FG, NONE
from zshpower.config import package

dt_omz = f"{FG.MAGENTA}robbyrussell{NONE}"
omz = f"{FG.MAGENTA}Oh My ZSH{NONE}"

options = f"""
{FG.MAGENTA}Welcome to the {package.info["pkg_name"]} options menu.{NONE}

Usage:
    {package.info['executable']} init [--omz]
    {package.info['executable']} sync
    {package.info['executable']} config (--open | --view)
    {package.info['executable']} activate
    {package.info['executable']} deactivate [--theme=<name>]
    {package.info['executable']} reset
    {package.info['executable']} uninstall
    {package.info['executable']} --help
    {package.info['executable']} --version
    {package.info['executable']} --credits

Arguments:
    {FG.CYAN}init{NONE} ---------- Installs the {package.info["name"]} settings.
    {FG.CYAN}sync{NONE} ---------- Synchronizes the machine's data with the {package.info["name"]} database.
    {FG.CYAN}activate{NONE} ------ Activate the {package.info["name"]} theme. ({omz}).
    {FG.CYAN}deactivate{NONE} ---- Deactivate the {package.info["name"]} theme and go back to the default. ({omz}).
    {FG.CYAN}reset{NONE} --------- Reset to default settings.
    {FG.CYAN}uninstall{NONE} ----- Uninstall the package {package.info["name"]}.
    {FG.CYAN}config{NONE} -------- The easiest way to edit and view the settings is through this option.

Options:
    {FG.CYAN}--help{NONE} --------- Show this screen.
    {FG.CYAN}--omz{NONE} ---------- Use this option if you want to use {package.info["name"]} with Oh My ZSH.
    {FG.CYAN}--open{NONE} --------- Open the configuration file in edit mode and perform the automatic update
                     when you exit.
    {FG.CYAN}--view{NONE} --------- View the configuration file on the terminal.
    {FG.CYAN}--theme=<name>{NONE} - Get the name of a theme available on Oh My ZSH [Default: {dt_omz}].
    {FG.CYAN}--version{NONE} ------ Show version.
    {FG.CYAN}--credits{NONE} ------ Show credits.
"""
