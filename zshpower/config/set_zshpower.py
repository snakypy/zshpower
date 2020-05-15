from zshpower.config import package

author = package.info["author"]["name"]
website_author = package.info["author"]["website"]
email = package.info["author"]["email"]

content = f"""#!/usr/bin/env zsh

# Information:
# ******************************************************************************
# Theme: {package.info["name"]}
# Description: Call script to start {package.info["name"]}.
# ******************************************************************************

export PATH="$PATH:$HOME/.local/bin"
function zshpower_precmd() {{
    if [[ ! -n $(which zshpower-shell) ]]; then
      PROMPT="$(zshpower-shell prompt)"
      RPROMPT="$(zshpower-shell rprompt)"
    else
      PROMPT='%F{{green}}%n%f@%F{{magenta}}%m%f %F{{blue}}%B%~%b%f %# '
      RPROMPT='[%F{{yellow}}%?%f]'
    fi
}}

function install_zshpower_precmd() {{
  for s in "${{precmd_functions[@]}}"; do
    if [ "$s" = "zshpower_precmd" ]; then
      return
    fi
  done
  precmd_functions+=(zshpower_precmd)
}}

if [ "$TERM" != "linux" ]; then
    install_zshpower_precmd
fi
"""
