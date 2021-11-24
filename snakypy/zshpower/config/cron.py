from snakypy.helpers.catches import whoami

from snakypy.zshpower import HOME
from snakypy.zshpower.config.base import Base

cron_content: str = f"""
#!/usr/bin/env zsh

PATH=\"{HOME}/.local/bin:/bin:/usr/local/bin:\\$PATH\"
export PATH

# Hourly in minute 0
# 0 * * * * {whoami()} {Base(HOME).sync_path}

# At minute 0 past every 2nd hour
# 0 */2 * * * {whoami()} {Base(HOME).sync_path}

# Daily at 7:00 am
# 0 07 * * * {whoami()} {Base(HOME).sync_path}

# You can use the site "https://crontab.guru" and some examples at "https://crontab.guru/examples.html"
"""

sync_content: str = f"""
#!/usr/bin/env zsh

PATH=\"{HOME}/.local/bin:/bin:/usr/local/bin:\\$PATH\"
export PATH

zshpower sync

"""
