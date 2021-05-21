from os.path import join

from snakypy.zshpower import __info__
from snakypy.zshpower.database.sql import sql


class Base:
    def __init__(self, home):
        self.HOME = home
        self.zshpower_home = join(
            self.HOME, f".{__info__['pkg_name']}", __info__["version"]
        )
        self.tbl_main = [item for item in sql().keys()][0]
        self.config_file = join(self.zshpower_home, "config.toml")
        self.data_root = join(self.zshpower_home, ".data")
        self.database_path = join(self.data_root, "db.sqlite3")
        self.sync_path = f"/usr/local/bin/{__info__['pkg_name']}_sync.sh"
        self.cron_path = f"/etc/cron.d/{__info__['pkg_name']}_task.sh"
        self.init_file = join(self.zshpower_home, "init.sh")
        self.zsh_rc = join(self.HOME, ".zshrc")
        self.omz_root = join(self.HOME, ".oh-my-zsh")
        self.themes_folder = join(self.omz_root, "custom/themes")
        self.theme_file = join(self.themes_folder, f"{__info__['pkg_name']}.zsh-theme")
        self.plugins = ("zsh-syntax-highlighting", "zsh-autosuggestions")
