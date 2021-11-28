from os.path import exists, isdir
from pydoc import pager

from snakypy.helpers import FG, pick
from snakypy.helpers.catches.finders import find_objects
from snakypy.helpers.console import printer
from snakypy.helpers.files import read_file
from snakypy.helpers.logging import Log

from snakypy.zshpower import __info__
from snakypy.zshpower.config.base import Base
from snakypy.zshpower.config.cron import cron_content, sync_content
from snakypy.zshpower.utils.check import checking_init
from snakypy.zshpower.utils.modifiers import command_root
from snakypy.zshpower.utils.process import open_file_with_editor


class Cron(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def manager(self, action=None) -> bool:

        if not isdir(self.cron_d_path):
            printer(
                f'It appears that your machine does not have Cron installed. {__info__["name"]} '
                f"could not find the folder. Aborted!",
                foreground=FG().WARNING,
            )
            return False

        try:
            if action == "create":

                if exists(self.sync_path) or exists(self.cron_path):
                    printer(
                        f"There is already a task in Cron for {__info__['name']}. Aborted!",
                        foreground=FG().WARNING,
                    )
                    return False

                printer(
                    f"Creating {__info__['name']} Task in Cron.",
                    foreground=FG().QUESTION,
                )

                cmd = f"""su -c 'echo "{sync_content}" > {self.sync_path}; chmod a+x {self.sync_path};
                                echo "{cron_content}" > {self.cron_path}; chmod a+x {self.cron_path}'
                                """
                command_root(cmd, logfile=self.logfile)

                printer(
                    f"{__info__['name']} Cron task created!", foreground=FG().FINISH
                )

                printer(
                    f"""
                ************************************ WARNING *********************************************
                    The task was created, however you need to see if the Cron service is started and
                    edit the "{self.cron_path}" file, determining a time to be executed.
                    To edit, run the command: {FG().CYAN}${__info__["executable"]} cron --open{FG().YELLOW}
                ******************************************************************************************
                """,
                    foreground=FG().YELLOW,
                )

                return True

            elif action == "remove":
                cron_file = find_objects(
                    self.cron_d_path, files=(f"{__info__['pkg_name']}_task.sh",)
                )
                task_run = find_objects(
                    "/etc/local/bin/", files=(f"{__info__['pkg_name']}_sync.sh",)
                )

                if not cron_file["files"] and not task_run["files"]:
                    printer(
                        f'There is no {__info__["name"]} task file in Cron to remove. Aborted!',
                        foreground=FG().WARNING,
                    )
                    return False

                if cron_file["files"] or task_run["files"]:
                    title = f"Really want to remove {__info__['name']} task from Cron?"
                    options = ["Yes", "No"]
                    reply = pick(title, options, colorful=True, index=True)
                    cmd = f"""su -c 'rm -f {self.sync_path} {self.cron_path}';"""

                    if reply is None or reply[0] == 1:
                        printer("Canceled by user.", foreground=FG().WARNING)
                        return False

                    command_root(cmd, logfile=self.logfile)

                    printer(
                        f"{__info__['name']} task has been removed from Cron!",
                        foreground=FG().FINISH,
                    )
                    return True
            return False
        except PermissionError as err:
            Log(filename=self.logfile).record(
                "No permission to write to directory /etc/crond.d or /usr/local/bin.",
                colorize=True,
                level="error",
            )
            raise PermissionError(
                "No permission to write to directory /etc/crond.d or /usr/local/bin.",
                err,
            )

    def run(self, arguments):
        checking_init(self.HOME, self.logfile)
        if arguments["--create"]:
            self.manager(action="create")
        elif arguments["--remove"]:
            self.manager(action="remove")
        elif arguments["--open"]:
            open_file_with_editor(
                self.config_file, file_common=self.cron_path, superuser=True
            )
        elif arguments["--view"]:
            try:
                read_config = read_file(self.cron_path)
                pager(read_config)
                return True
            except FileNotFoundError:
                printer(
                    f'ZSHPower task file does not exist in Cron. Use: "{__info__["executable"]} cron --create"',
                    foreground=FG().WARNING,
                )
            return False
