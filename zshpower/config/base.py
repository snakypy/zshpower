class Base:
    def __init__(self, home):
        from zshpower.config import package
        from zshpower import __version__
        from os.path import join

        self.HOME = home
        self.config_root = join(
            self.HOME, f".{package.info['pkg_name']}/config/{__version__}"
        )
        self.data_root = f".{package.info['pkg_name']}/data"
        self.database_name = 'database.sqlite3'
        self.init_file = join(self.HOME, f".{package.info['pkg_name']}/init")
        self.config_file = join(self.config_root, "config.toml")
        self.zsh_rc = join(self.HOME, ".zshrc")
        self.omz_root = join(self.HOME, ".oh-my-zsh")
        self.themes_folder = join(self.omz_root, "custom/themes")
        self.theme_file = join(
            self.themes_folder, f"{package.info['pkg_name']}.zsh-theme"
        )
        self.plugins = ("zsh-syntax-highlighting", "zsh-autosuggestions")
