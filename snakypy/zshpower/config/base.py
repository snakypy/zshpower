from os.path import join

from snakypy.helpers.logging import Log
from snakypy.helpers.path import create as create_path

from snakypy.zshpower import __info__
from snakypy.zshpower.database.sql import sql


class Base:
    def __init__(self, home):
        self.HOME = home
        self.zshpower_home = join(self.HOME, f".{__info__['pkg_name']}")
        self.tbl_main = [item for item in sql().keys()][0]
        self.config_root = join(self.zshpower_home, "config")
        self.lib_root = join(self.zshpower_home, "lib")
        self.config_file = join(self.config_root, "zshpower.toml")
        self.database_root = join(self.zshpower_home, ".database")
        self.cache_root = join(self.zshpower_home, ".cache")
        self.logfile = join(self.zshpower_home, ".cache", "zshpower.log")
        self.database_path = join(self.database_root, "zshpower.sqlite3")
        self.sync_path = f"/usr/local/bin/{__info__['pkg_name']}_sync.sh"
        self.cron_d_path = "/etc/cron.d/"
        self.cron_path = join(self.cron_d_path, f"{__info__['pkg_name']}_task.sh")
        self.lib_main = join(self.lib_root, "main.lib")
        self.zsh_rc = join(self.HOME, ".zshrc")
        self.omz_root = join(self.HOME, ".oh-my-zsh")
        self.themes_folder = join(self.omz_root, "custom/themes")
        self.theme_symlink = join(
            self.themes_folder, f"{__info__['pkg_name']}.zsh-theme"
        )
        self.source_code = f".{__info__['pkg_name']}/lib/main.lib"
        self.plugins = ("zsh-syntax-highlighting", "zsh-autosuggestions")
        create_path(self.cache_root)
        self.log = Log(self.logfile)
