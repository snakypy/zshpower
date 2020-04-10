from zshpower.config import package

author = package.info["author"]["name"]
website_author = package.info["author"]["website"]
email = package.info["author"]["email"]

content = f"""#!/usr/bin/env zsh

# Information:
# ******************************************************************************
# Theme: {package.info["name"]}
# Description: Call script to start {package.info["name"]}.
# Author: {author}, {website_author}


export PATH="$PATH:$HOME/.local/bin"
function set_zshpower () {{
    PROMPT="$(zshpower-shell prompt)"
    RPROMPT="$(zshpower-shell rprompt)"
}}
autoload add-zsh-hook
add-zsh-hook precmd set_zshpower
"""
