from datetime import datetime
from zshpower import __version__


content = f"""# Generate by: ZSHPower - D{datetime.today().isoformat()}
# Version: {__version__}
# ---------------------------------------------------------------------
# For more information, see the documentation at:
# https://github.com/snakypy/zshpower#configuration-file

[general]
jump_line.enable = true
config.editor = "vim"
separator.element = "-"
separator.color = "white"
position = ["virtualenv", "python", "package", "docker", "nodejs", "git"]

[username]
enable = false
color = "cyan"

[hostname]
enable = false
color = "magenta"
prefix.color = "white"
prefix.text = "at"

[directory]
truncation_length = 1
symbol = "\\ufc6e"
color = "cyan"
prefix.color = "white"
prefix.text = "in"

[git]
enable = true
symbol = "\\uf418"
branch.color = "cyan"
color.symbol = "magenta"
prefix.color = "white"
prefix.text = "on"

[git.status]
symbols.enable = true
symbol.clean = "\\uf62c"
symbol.added = "\\ufc03"
symbol.modified = "\\ufc07"
symbol.deleted = "\\ufbc7"
symbol.renamed = "\\uf101"
symbol.unmerged = "\\uf6fb"
symbol.untracked = "\\uf41e"
symbol.copied = "\\ufab1"
symbol.ahead = "\\uf55c"
symbol.behind = "\\uf544"
symbol.diverged = "\\ufb15"
symbol.conflicts = "\\uf0e7"

[command]
new_line.enable = true
symbol = "\\uf553"
color = "green"
error.symbol = "\\uf553"
error.color = "red"

[package]
enable = true
symbol = "\\uf8d6"
color = "red"
prefix.color = "white"
prefix.text = "is"

[docker]
symbol = "\\uf308"
color = "blue"
prefix.color = "white"
prefix.text = "on"
version.enable = true
version.micro.enable = true

[nodejs]
symbol = "\\uf898"
color = "green"
prefix.color = "white"
prefix.text = "on"
version.enable = true
version.micro.enable = true

[python]
symbol = "\\uf81f"
color = "yellow"
prefix.color = "white"
prefix.text = "via"
version.enable = true
version.micro.enable = true

[virtualenv]
enable = true
symbol = "\\ufcc2"
involved = "()"
color = "yellow"
prefix.color = "white"
prefix.text = "via"

[virtualenv.name]
normal.enable = true
text = "venv"

[timer]
enable = true
symbol = "\\uf43a"
color = "blue"
seconds.enable = false
"""
