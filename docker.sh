#!/usr/bin/env zsh

cat << EOF > /root/.zshrc
 source $HOME/.zshpower/init
EOF

poetry shell
