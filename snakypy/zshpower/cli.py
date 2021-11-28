"""CLI - Command Line Interface"""
from sys import exit

from snakypy.helpers import FG, printer

from snakypy.zshpower.commands.cron import Cron

try:
    from snakypy.helpers.decorators import only_linux
except KeyboardInterrupt:
    pass
from snakypy.zshpower import HOME
from snakypy.zshpower.commands.activate import ActivateCommand
from snakypy.zshpower.commands.config import ConfigCommand
from snakypy.zshpower.commands.credits import CreditsCommand
from snakypy.zshpower.commands.deactivate import DeactivateCommand
from snakypy.zshpower.commands.init import InitCommand
from snakypy.zshpower.commands.logs import LogsCommand
from snakypy.zshpower.commands.reset import ResetCommand
from snakypy.zshpower.commands.sync import Sync
from snakypy.zshpower.commands.uninstall import UninstallCommand
from snakypy.zshpower.utils.catch import arguments
from snakypy.zshpower.utils.decorators import assign_cli

# Get arguments Docopt
args: dict = arguments()


@assign_cli(args, "init")
def run_init() -> None:
    InitCommand(HOME).run(args, reload=True)


@assign_cli(args, "config")
def run_config() -> None:
    ConfigCommand(HOME).run(args)


@assign_cli(args, "activate")
def run_activate() -> None:
    ActivateCommand(HOME).run()


@assign_cli(args, "deactivate")
def run_deactivate() -> None:
    DeactivateCommand(HOME).run(args)


@assign_cli(args, "reset")
def run_reset() -> None:
    ResetCommand(HOME).run(args)


@assign_cli(args, "uninstall")
def run_uninstall() -> None:
    UninstallCommand(HOME).run()


@assign_cli(args, "sync")
def run_sync() -> None:
    Sync(HOME).run()


@assign_cli(args, "cron")
def run_cron() -> None:
    Cron(HOME).run(args)


@assign_cli(args, "logs")
def run_logs() -> None:
    LogsCommand(HOME).run(args)


@assign_cli(args, "--credits")
def run_credits() -> None:
    CreditsCommand().run()


# @silent_errors
@only_linux
def main() -> None:
    try:
        run_init()
        run_config()
        run_activate()
        run_deactivate()
        run_reset()
        run_uninstall()
        run_sync()
        run_cron()
        run_logs()
        run_credits()
    except KeyboardInterrupt:
        printer("Aborted by user.", foreground=FG().WARNING)
        exit(0)
