from datetime import datetime

config_content: str = f"""# Generate by: ZSHPower - D{datetime.today().isoformat()}
# ---------------------------------------------------------------------
# For more information, see the documentation at:
# https://github.com/snakypy/zshpower#configuration-file

[general]
color.enable = true
jump_line.enable = true
config.editor = "vim"
separator.element = "∙"
separator.color = "negative"
position = [
    "virtualenv",
    "python",
    "package",
    "nodejs",
    "rust",
    "golang",
    "java",
    "php",
    "ruby",
    "elixir",
    "julia",
    "dart",
    "dotnet",
    "docker",
    "perl",
    "scala",
    "cmake",
    "crystal",
    "deno",
    "erlang",
    "helm",
    "kotlin",
    "nim",
    "ocaml",
    "vagrant",
    "zig",
    "gulp",
    "git",
    ]

[command]
new_line.enable = true
symbol = "\\u276f"
color = "green"
error.symbol = "\\u276f"
error.color = "red"

[cmake]
symbol = "\\ufa35"
color = "green"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[crystal]
symbol = "\\uf7d7"
color = "magenta"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[dart]
symbol = "\\ue798"
color = "cyan"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[deno]
symbol = "\\u1f995"
color = "green"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[directory]
truncation_length = 1
symbol = "\\ue5fe"
color = "cyan"
prefix.color = "negative"
prefix.text = "in"

[docker]
symbol = "\\uf308"
color = "cyan"
prefix.color = "negative"
prefix.text = "on"
version.enable = false
version.micro.enable = true

[dotnet]
symbol = "\\ue77f"
color = "cyan"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[elixir]
symbol = "\\ue62d"
color = "blue"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[erlang]
symbol = "\\ue7b1"
color = "red"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[git]
enable = true
symbol = "\\ue725"
branch.color = "cyan"
color.symbol = "magenta"
prefix.color = "negative"
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

[golang]
symbol = "\\ue627"
color = "cyan"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[gulp]
symbol = "\\ue763"
color = "red"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[helm]
symbol = "\\ufd31"
color = "cyan"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[hostname]
enable = false
symbol = "\\ue0a2"
color = "magenta"
prefix.color = "negative"
prefix.text = "at"

[java]
symbol = "\\ue256"
color = "red"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[julia]
symbol = "\\ue624"
color = "blue"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[kotlin]
symbol = "\\ue622"
color = "blue"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[nim]
symbol = "\\uf6a4"
color = "yellow"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[nodejs]
symbol = "\\uf898"
color = "green"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[ocaml]
symbol = "?"
color = "yellow"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[package]
enable = false
symbol = "\\uf8d6"
display = ["python", "node", "rust", "scala", "crystal", "helm"]
color = "red"
prefix.color = "negative"
prefix.text = "is"

[perl]
symbol = "\\ue769"
color = "blue"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[php]
symbol = "\\ue608"
color = "magenta"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[python]
symbol = "\\uf81f"
color = "yellow"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[python.virtualenv]
enable = false
symbol = "\\uf7c9"
involved = "[]"
color = "yellow"
prefix.color = "negative"
prefix.text = "via"

[python.virtualenv.name]
normal.enable = true
text = "venv"

[python.virtualenv.poetry]
py.enable = true
hash.enable = true

[ruby]
symbol = "\\ue21e"
color = "red"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[rust]
symbol = "\\ue7a8"
color = "red"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[scala]
symbol = "\\ue737"
color = "red"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[timer]
enable = false
symbol = "\\uf43a"
color = "blue"
seconds.enable = false

[took]
enable = false
symbol = "\\ufbab"
text = "took"
color = "yellow"
involved = "[]"
show_greater_than = 1

[username]
enable = false
symbol = "\\uf007"
color = "cyan"

[vagrant]
symbol = "\\ue62b"
color = "yellow"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[zig]
symbol = "\\ue00a"
color = "yellow"
prefix.color = "negative"
prefix.text = "via"
version.enable = false
version.micro.enable = true
"""
