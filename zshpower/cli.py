"""CLI - Command Line Interface"""
from snakypy.utils.decorators import only_for_linux
from zshpower.commands.init import InitCommand
from zshpower.commands.activate import ActivateCommand
from zshpower.commands.config import ConfigCommand
from zshpower.commands.deactivate import DeactivateCommand
from zshpower.commands.reset import ResetCommand
from zshpower.commands.uninstall import UninstallCommand
from zshpower.commands.credits import CreditsCommand
from zshpower.utils.decorators import assign_cli
from zshpower.utils.catch import arguments
from zshpower import HOME


# Get arguments Docopt
args = arguments()


@assign_cli(args, "init")
def run_init():
    InitCommand(HOME).main(args, reload=True, message=True)


@assign_cli(args, "config")
def run_config():
    ConfigCommand(HOME).main(args)


@assign_cli(args, "activate")
def run_activate():
    ActivateCommand(HOME).main()


@assign_cli(args, "deactivate")
def run_deactivate():
    DeactivateCommand(HOME).main(args)


@assign_cli(args, "reset")
def run_reset():
    ResetCommand(HOME).main()


@assign_cli(args, "uninstall")
def run_uninstall():
    UninstallCommand(HOME).main()


@assign_cli(args, "--credits")
def run_credits():
    CreditsCommand().main()


@only_for_linux
def main():
    run_init()
    run_config()
    run_activate()
    run_deactivate()
    run_reset()
    run_uninstall()
    run_credits()
