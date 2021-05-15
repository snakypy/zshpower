FROM python:3.9
USER root
WORKDIR /snakypy/zshpower
ENV LOCAL_BIN=/root/.local/bin
RUN apt-get update \
&& apt-get install zsh vim -y \
&& export PATH=$PATH:$LOCAL_BIN \
&& pip install poetry \
&& rm -rf /var/cache/apt/*
ADD . /snakypy/zshpower
RUN cd /snakypy/zshpower \
&& poetry install \
&& echo "[[ -f /root/.zshpower/0.7.0/init.sh ]] && . /root/.zshpower/0.7.0/init.sh" > /root/.zshrc \
&& chmod +x docker.sh
CMD poetry shell
