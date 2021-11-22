from os.path import exists

from snakypy.helpers import FG, pick
from snakypy.helpers.console import printer
from snakypy.helpers.logging import Log

from snakypy.zshpower import __info__
from snakypy.zshpower.config.base import Base
from snakypy.zshpower.config.cron import cron_content, sync_content
from snakypy.zshpower.utils.check import checking_init
from snakypy.zshpower.utils.modifiers import create_file_superuser


class Cron(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def manager(self, action=None):
        try:
            if action == "create":
                printer(
                    f"Creating {__info__['name']} Task in Cron.",
                    foreground=FG().QUESTION,
                )
                cmd = f"""su -c 'echo "{sync_content}" > {self.sync_path}; chmod a+x {self.sync_path};
                echo "{cron_content}" > {self.cron_path};'
                """
                if exists(self.sync_path) or exists(self.cron_path):
                    printer(
                        f"There is already a task in Cron for {__info__['name']}. Aborted!",
                        foreground=FG().WARNING,
                    )
                    return False
                create_file_superuser(cmd, self.logfile)
                printer(
                    f"{__info__['name']} Cron task created!", foreground=FG().FINISH
                )
                printer(
                    f"""
                ************************************ WARNING *********************************************
                    The task was created, however you need to see if the Cron service is started and
                    edit the {self.cron_path} file, determining a time to be executed.
                ******************************************************************************************
                """,
                    foreground=FG().WARNING,
                )

            elif action == "remove":
                title = f"Really want to remove {__info__['name']} task from Cron?"
                options = ["Yes", "No"]
                reply = pick(
                    title, options, colorful=True, index=True, ctrl_c_message=True
                )
                cmd = f"""su -c 'rm -f {self.sync_path} {self.cron_path}';"""
                if reply is None or reply[0] == 1:
                    printer("Canceled by user", foreground=FG().WARNING)
                    return False
                create_file_superuser(cmd, self.logfile)
                printer(
                    f"{__info__['name']} task has been removed from Cron!",
                    foreground=FG().FINISH,
                )

        except PermissionError:
            Log(filename=self.logfile).record(
                f"No permission to write to directory /etc/crond.d or /usr/local/bin.",
                colorize=True,
                level="error",
            )
            raise PermissionError(
                "No permission to write to directory /etc/crond.d or /usr/local/bin."
            )

    def run(self, arguments) -> None:
        checking_init(self.HOME, self.logfile)
        if arguments["--create"]:
            # self.manager(action="create")
            print("1")
        elif arguments["--remove"]:
            # self.manager(action="remove")
            print("2")
