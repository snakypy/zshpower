from subprocess import call as subprocess_call

# from zshpower.utils.check import is_tool, tools_requirements


def reload_zsh():
    subprocess_call("exec zsh", shell=True)


def change_shell():
    from snakypy import printer
    from zshpower.utils.catch import current_user, current_shell
    from snakypy.ansi import FG

    if current_shell()[0] != "zsh":
        try:
            subprocess_call(f"chsh -s $(which zsh) {current_user()}", shell=True)
        except KeyboardInterrupt:
            printer("Canceled by user", foreground=FG.WARNING)


def shell_command(cmd):
    from subprocess import PIPE, Popen as subprocess_popen

    p = subprocess_popen(
        cmd, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True
    )
    output, err = p.communicate()
    return output.replace("\n", ""), err


# # TODO: This may be for the future, but not now.
# #
# def bash_command(cmd):
#     subprocess_popen(["/bin/bash", "-c", cmd])

# def systemctl_is_active(service):
#     process = subprocess_popen(
#         ["systemctl", "is-active", service], stdout=PIPE, universal_newlines=True
#     )
#     output, err = process.communicate()
#     return output.replace("\n", ""), err
