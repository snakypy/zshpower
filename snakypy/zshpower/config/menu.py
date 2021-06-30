from snakypy.helpers.ansi import FG, NONE

from snakypy.zshpower import __info__

dt_omz: str = f"{FG().MAGENTA}robbyrussell{NONE}"
omz: str = f"{FG().MAGENTA}Oh My ZSH{NONE}"

options: str = f"""
{FG().MAGENTA}Welcome to the {__info__["pkg_name"]} options menu.{NONE}

Usage:
    {__info__['executable']} init [--omz]
    {__info__['executable']} sync
    {__info__['executable']} config (--open | --view)
    {__info__['executable']} logs (--view | --clean)
    {__info__['executable']} activate
    {__info__['executable']} deactivate [--theme=<name>]
    {__info__['executable']} reset (--config | --db)
    {__info__['executable']} uninstall
    {__info__['executable']} --help
    {__info__['executable']} --version
    {__info__['executable']} --credits

Arguments:
    {FG().CYAN}init{NONE} ---------- Installs the {__info__["name"]} settings.
    {FG().CYAN}sync{NONE} ---------- Synchronizes the machine's data with the {__info__["name"]} database.
    {FG().CYAN}activate{NONE} ------ Activate the {__info__["name"]} theme. ({omz}).
    {FG().CYAN}deactivate{NONE} ---- Deactivate the {__info__["name"]} theme and go back to the default. ({omz}).
    {FG().CYAN}reset{NONE} --------- Reset to default settings.
    {FG().CYAN}uninstall{NONE} ----- Uninstall the package {__info__["name"]}.
    {FG().CYAN}config{NONE} -------- The easiest way to edit and view the settings is through this option.
    {FG().CYAN}logs{NONE} ---------- Shows {__info__["name"]} activity logs.

Options:
    {FG().CYAN}--help{NONE} --------- Show this screen.
    {FG().CYAN}--omz{NONE} ---------- Use this option if you want to use {__info__["name"]} with Oh My ZSH.
    {FG().CYAN}--open{NONE} --------- Open the configuration file in edit mode and perform the automatic update
                     when you exit.
    {FG().CYAN}--view{NONE} --------- View the configuration file on the terminal.
    {FG().CYAN}--config{NONE} ------- Restores the configuration file.
    {FG().CYAN}--db{NONE} ----------- Restores the database.
    {FG().CYAN}--theme=<name>{NONE} - Get the name of a theme available on Oh My ZSH [Default: {dt_omz}].
    {FG().CYAN}--version{NONE} ------ Show version.
    {FG().CYAN}--credits{NONE} ------ Show credits.
"""
