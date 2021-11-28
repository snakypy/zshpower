import os
from shutil import which
from subprocess import call
from time import sleep

from snakypy.helpers import FG, printer
from snakypy.helpers.catches import is_tool, shell, whoami
from snakypy.helpers.files import read_file
from snakypy.helpers.logging import Log
from tomlkit import parse as toml_parse

from snakypy.zshpower.utils.catch import get_key


def reload_zsh(sleep_timer=None, message=False) -> None:
    """
    Reload ZSH
    """
    if message:
        printer("Restarting terminal, wait...", foreground=FG().QUESTION)
    if sleep_timer:
        sleep(sleep_timer)
    call("exec zsh", shell=True)


def change_shell(logfile) -> bool:
    """
    Function that checks if the shell is not ZSH and requests changes to it.
    """

    try:
        if shell() != "zsh":
            printer(
                "Changing the shell from Bash to ZSH (Root password required). [Press Ctrl+C to cancel]",
                foreground=FG().QUESTION,
            )
            if which("chsh"):
                call(f"chsh -s $(which zsh) {whoami()}", shell=True)
            elif which("usermod"):
                call(f'su -c "usermod -s $(which zsh) {whoami()}"', shell=True)
            else:
                return False
            return True
        return False
    except KeyboardInterrupt:
        Log(filename=logfile).record(
            f"Shell change canceled by user ({whoami()})",
            colorize=True,
            level="warning",
        )
        printer("Canceled by user.", foreground=FG().WARNING)
    return False


def open_file_with_editor(toml_file, file_common=None, superuser: bool = False) -> None:
    """
    Opens file with a certain editor according to what is informed in the ZSHPower configuration file
    """

    def editor_run(editor, config, get_superuser=superuser) -> bool:
        if which(editor):
            get_editor = os.environ.get("EDITOR", editor)
            with open(config) as f:
                # TODO: It is not accepting the "command_root" function. Solve.
                if get_superuser:
                    try:
                        cmd = f"""su -c '{get_editor} {f.name}';"""
                        printer(
                            "[ Enter the machine superuser password ]",
                            foreground=FG().WARNING,
                        )
                        call(cmd, shell=True, universal_newlines=True)
                        return True
                    except KeyboardInterrupt:
                        printer("Aborted by user.", foreground=FG().WARNING)
                        return False
                else:
                    call([get_editor, f.name])
                    return True
        return False

    def condition(editor):
        if file_common:
            return editor_run(editor, file_common, get_superuser=superuser)
        return editor_run(editor, toml_file, get_superuser=superuser)

    try:
        read_conf = read_file(toml_file)
        parsed = dict(toml_parse(read_conf))
        get_editor_name = get_key(parsed, "general", "config", "editor")
        if get_editor_name and get_editor_name != {}:
            condition(get_editor_name)
        else:
            editors = ("vim", "nano", "emacs", "micro", "vi")
            for edt in editors:
                if is_tool(edt):
                    condition(edt)
                    break
    except FileNotFoundError:
        printer(
            'ZSHPower task file does not exist in Cron. Use: "zshpower cron --create"',
            foreground=FG().WARNING,
        )
