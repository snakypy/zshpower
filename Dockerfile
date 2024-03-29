FROM python:3.9
USER root
WORKDIR /snakypy/zshpower
ENV LOCAL_BIN=/root/.local/bin
RUN apt-get update \
	&& apt-get install zsh vim curl git sqlite3 -y \
	&& export PATH=$PATH:$LOCAL_BIN \
	&& pip install poetry \
	&& rm -rf /var/cache/apt/*
ADD . /snakypy/zshpower
RUN cd /snakypy/zshpower \
  && poetry install \
	&& echo 'eval "$(zshpower init --path)"' >> /root/.zshrc
CMD poetry shell
