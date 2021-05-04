"""CLI - Command Line Interface"""
try:
    from snakypy.utils.decorators import only_for_linux
except KeyboardInterrupt:
    pass
from zshpower.utils.decorators import silent_errors
from zshpower.utils.decorators import assign_cli
from zshpower.utils.catch import arguments
from zshpower import HOME


# Get arguments Docopt
args = arguments()


@assign_cli(args, "init")
def run_init():
    from zshpower.commands.init import InitCommand

    InitCommand(HOME).run(args, reload=True, message=True)


@assign_cli(args, "config")
def run_config():
    from zshpower.commands.config import ConfigCommand

    ConfigCommand(HOME).run(args)


@assign_cli(args, "activate")
def run_activate():
    from zshpower.commands.activate import ActivateCommand

    ActivateCommand(HOME).run()


@assign_cli(args, "deactivate")
def run_deactivate():
    from zshpower.commands.deactivate import DeactivateCommand

    DeactivateCommand(HOME).run(args)


@assign_cli(args, "reset")
def run_reset():
    from zshpower.commands.reset import ResetCommand

    ResetCommand(HOME).run(args)


@assign_cli(args, "uninstall")
def run_uninstall():
    from zshpower.commands.uninstall import UninstallCommand

    UninstallCommand(HOME).run()


@assign_cli(args, "sync")
def run_sync():
    from zshpower.commands.sync import Sync

    Sync(HOME).run()


@assign_cli(args, "--credits")
def run_credits():
    from zshpower.commands.credits import CreditsCommand

    CreditsCommand().run()


@silent_errors
@only_for_linux
def main():
    run_init()
    run_config()
    run_activate()
    run_deactivate()
    run_reset()
    run_uninstall()
    run_sync()
    run_credits()
