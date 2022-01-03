from snakypy.helpers.checking import whoami

from snakypy.zshpower import HOME

cron_content: str = f"""# ZSHPower Tasks  - BEGIN
SHELL=/bin/zsh
PATH=\"\\$PATH:/bin:/usr/local/bin:{HOME}/.local/bin\"
export PATH


## ZSHPower Tasks (Every 2 minutes of every hour) ##
# */2 * * * * {whoami()} zshpower sync
# */2 * * * * {whoami()} zshpower logs --clean

## ZSHPower Tasks (Every 5 minutes of every hour) ##
# */5 * * * * {whoami()} zshpower sync
# */5 * * * * {whoami()} zshpower logs --clean

## ZSHPower Tasks (Every 10 minutes of every hour) ##
# */10 * * * * {whoami()} zshpower sync
# */10 * * * * {whoami()} zshpower logs --clean

## ZSHPower Tasks (Every 30 minutes of every hour) ##
# */30 * * * * {whoami()} zshpower sync
# */30 * * * * {whoami()} zshpower logs --clean

## ZSHPower Tasks (At minute 0 past every 2nd hour) ##
# 0 */2 * * * {whoami()} zshpower sync
# 0 */2 * * * {whoami()} zshpower logs --clean

## ZSHPower Tasks (Daily at 7:00 am) ##
# 0 07 * * * {whoami()} zshpower sync
# 0 07 * * * {whoami()} zshpower logs --clean

# ZSHPower Tasks (Monthly)
# 0 0 1 * * {whoami()} zshpower sync
# 0 0 1 * * {whoami()} zshpower logs --clean

# ZSHPower Tasks (Weekly)
# 0 0 * * 1 {whoami()} zshpower sync
# 0 0 * * 1 {whoami()} zshpower logs --clean

# ZSHPower Tasks (Daily)
# 0 0 * * * {whoami()} zshpower sync
# 0 0 * * * {whoami()} zshpower logs --clean

# You can use the site "https://crontab.guru" and some examples at "https://crontab.guru/examples.html"
#
# ZSHPower Tasks - END"""

# sync_content: str = f"""
# #!/usr/bin/env zsh
#
# SHELL=/bin/zsh
# PATH=\"\\$PATH:/bin:/usr/local/bin:{HOME}/.local/bin\"
# export PATH
#
# if [[ -f $(which zshpower) ]]; then
#   zshpower sync
# else
#     echo "Not found command 'zshpower'."
# fi
#
# """
