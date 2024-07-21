FROM ubuntu:bionic

ENV DEBIAN_FRONTEND noninteractive

RUN sed -re 's/([a-z]{2}.)?archive.ubuntu.com/mirror.kakao.com/g' -e 's/security.ubuntu.com/mirror.kakao.com/g' -i.bak /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-virtualenv gunicorn3

# Setup flask application
RUN mkdir -p /deploy/app
COPY gunicorn_config.py /deploy/gunicorn_config.py
COPY app /deploy/app
RUN python3 -m pip install -U pip setuptools wheel
RUN python3 -m pip install -r /deploy/app/requirements.txt
RUN python3 -m pip install --upgrade psutil
WORKDIR /deploy/app

EXPOSE 8080

# Start gunicorn
CMD ["/usr/bin/gunicorn3", "--config", "/deploy/gunicorn_config.py", "hello:app"]
