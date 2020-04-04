from datetime import datetime
from zshpower import __version__, __pkginfo__


def config_content():
    date_format = datetime.today().isoformat()
    data = f"""# Generate by: ZSHPower - D{date_format}
# Version: {__version__}
# ---------------------------------------------------------------------
# For more information, see the documentation at:
# https://github.com/snakypy/zshpower#configuration-file

[general]
jump_line.enable = true
separator.element = "-"
separator.color = "white"
position = ["package", "virtualenv", "python", "git"]

[username]
enable = false
color = "cyan"

[hostname]
enable = false
color = "magenta"
prefix.color = "green"
prefix.text = "at"

[directory]
truncation_length = 2
symbol = "\\ufc6e"
color = "cyan"
prefix.color = "green"
prefix.text = "in"

[git]
enable = true
symbol = "\\uf418"
branch.color = "cyan"
color.symbol = "white"
prefix.color = "green"
prefix.text = "on"

[git.status]
symbols.enable = true
symbol.clean = "\\uf62c"
symbol.added = "\\ufc03"
symbol.modified = "\\ufba8"
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

[pyproject]
enable = true
symbol = "\\uf8d6"
color = "red"
prefix.color = "green"
prefix.text = "on"

[python]
symbol = "\\uf81f"
color = "yellow"
prefix.color = "green"
prefix.text = "via"
version.enable = true
version.micro.enable = true

[virtualenv]
enable = true
symbol = "\\uf10c"
involved = "()"
color = "yellow"
prefix.color = "green"
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
    return data


def zshrc_content(omz_root):
    data = f"""# Generate by: ZSHPower
# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="{omz_root}"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="{__pkginfo__['pkg_name']}"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in ~/.oh-my-zsh/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS=true

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for
# completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large
# repositories much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution
# time stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git python django pip pep8 autopep8)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
    """
    return data


def theme_content():
    author = __pkginfo__["author"]["name"]
    website_author = __pkginfo__["author"]["website"]
    email = __pkginfo__["author"]["email"]
    content = f"""#!/usr/bin/env zsh

# Information:
# ******************************************************************************
# Theme: {__pkginfo__["name"]}
# Description: {__pkginfo__["description"]}
# Author: {author}, {website_author}

# LICENSE:
#    MIT License
#
#    Copyright (c) 2020-present {author} <{email}>
#
#    Permission is hereby granted, free of charge, to any person obtaining a copy
#    of this software and associated documentation files (the "Software"), to deal
#    in the Software without restriction, including without limitation the rights
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#    copies of the Software, and to permit persons to whom the Software is
#    furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in all
#    copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#    SOFTWARE.
# ******************************************************************************

function set_zshpower () {{
    PROMPT="$(zshpower-shell prompt)"
    RPROMPT="$(zshpower-shell rprompt)"
}}
autoload add-zsh-hook
add-zsh-hook precmd set_zshpower
    """
    return content
