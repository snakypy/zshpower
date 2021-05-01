from zshpower.utils.catch import current_user
from zshpower.config.base import Base
from zshpower import HOME

cron_content = f"""
#!/bin/sh

PATH="~/.local/bin:/bin:/usr/local/bin:\\$PATH"
export PATH

# Hourly in minute 0
# 0 * * * * {current_user()} {Base(HOME).sync_path}

# At minute 0 past every 2nd hour
# 0 */2 * * * {current_user()} {Base(HOME).sync_path}

# Daily at 7:00 am
# 0 07 * * * {current_user()} {Base(HOME).sync_path}

# You can use the site "https://crontab.guru" and some examples at "https://crontab.guru/examples.html"
"""

sync_content = """
#!/bin/sh

PATH="~/.local/bin:/bin:/usr/local/bin:\\$PATH"
export PATH

zshpower sync

"""
