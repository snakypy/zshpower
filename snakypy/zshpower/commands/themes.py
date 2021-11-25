# from subprocess import call
#
# from snakypy.helpers.ansi import FG
# from snakypy.helpers.console.display import printer
#
# from snakypy.zshpower.config.base import Base
# from snakypy.zshpower.utils.catch import get_zsh_theme
# from snakypy.zshpower.utils.check import checking_init
#
# # TODO: It will still be decided whether to implement
# class Theme(Base):
#     def __init__(self, home):
#         Base.__init__(self, home)
#
#     def run(self, arguments):
#         checking_init(self.HOME, self.logfile)
#
#         zshrc_omz = get_zsh_theme(self.zsh_rc, self.logfile)
#
#         if not zshrc_omz:
#             return printer(
#                 "Command not available. Only with Oh My ZSH installed. Aborted.",
#                 foreground=FG().WARNING,
#             )
#
#         if zshrc_omz and arguments["--list"]:
#             call(["zsh", "-i", "-c", "omz theme list"])
