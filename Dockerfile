FROM python:3
USER root
WORKDIR /zshpower
ENV LOCAL_BIN=/root/.local/bin
RUN apt-get update \
&& apt-get install zsh vim -y \
&& export PATH=$PATH:$LOCAL_BIN \
&& pip install poetry \
&& rm -rf /var/cache/apt/*
ADD . /zshpower
RUN cd /zshpower \
&& poetry install \
&& echo "[[ -f /root/.zshpower/init ]] && . /root/.zshpower/init" > /root/.zshrc \
&& chmod +x docker.sh
CMD poetry shell
