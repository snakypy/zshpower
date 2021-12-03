from snakypy.helpers.catches import whoami

from snakypy.zshpower import HOME

cron_content: str = f"""# ZSHPower Task Synchronize database - BEGIN
SHELL=/bin/zsh
PATH=\"\\$PATH:/bin:/usr/local/bin:{HOME}/.local/bin\"
export PATH

# Every 2 minutes of every hour.
# */2 * * * * {whoami()} zshpower sync

# Every 5 minutes of every hour.
# */5 * * * * {whoami()} zshpower sync

# Every 10 minutes.
# */10 * * * * {whoami()} zshpower sync

# Every 30 minutes.
# */30 * * * * {whoami()} zshpower sync

# At minute 0 past every 2nd hour
# 0 */2 * * * {whoami()} zshpower sync

# Daily at 7:00 am
# 0 07 * * * {whoami()} zshpower sync

# You can use the site "https://crontab.guru" and some examples at "https://crontab.guru/examples.html"
#
# ZSHPower Task Synchronize database - END"""

sync_content: str = f"""
#!/usr/bin/env zsh

SHELL=/bin/zsh
PATH=\"\\$PATH:/bin:/usr/local/bin:{HOME}/.local/bin\"
export PATH

if [[ -f $(which zshpower) ]]; then
  zshpower sync
else
    echo "Not found command 'zshpower'."
fi

"""
