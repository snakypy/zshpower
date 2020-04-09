from snakypy import printer
from snakypy.ansi import FG
from zshpower.config.base import Base
from snakypy.path import create as snakypy_path_create
from snakypy.file import create as snakypy_file_create
from zshpower.utils.check import tools_requirements
from zshpower.config.config import content as config_content
from zshpower.config.zshrc import content as zshrc_content
from zshpower.config.zsh_theme import content as zshpower_theme_content
from zshpower.utils.process import change_shell, reload_zsh
from zshpower.utils.shift import (
    create_config,
    omz_install,
    omz_install_plugins,
    install_fonts,
    create_zshrc,
    change_theme_in_zshrc,
    add_plugins_zshrc,
)


class InitCommand(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def main(self, reload=False, message=False):
        tools_requirements("git", "vim", "zsh")
        snakypy_path_create(self.config_root)
        create_config(config_content, self.config)
        omz_install(self.omz_root)
        omz_install_plugins(self.omz_root, self.plugins)
        install_fonts(self.HOME)
        create_zshrc(zshrc_content(self.omz_root), self.zsh_rc)
        change_theme_in_zshrc(self.zsh_rc, "zshpower")
        add_plugins_zshrc(self.zsh_rc)
        snakypy_file_create(zshpower_theme_content, self.theme_file, force=True)
        change_shell()
        printer("Done!", foreground=FG.FINISH) if message else None
        reload_zsh() if reload else None
