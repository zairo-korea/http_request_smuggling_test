FROM ubuntu:bionic

ARG base_domain
ARG first_subdomain
ARG second_subdomain

ENV DEBIAN_FRONTEND noninteractive

RUN sed -re 's/([a-z]{2}.)?archive.ubuntu.com/mirror.kakao.com/g' -e 's/security.ubuntu.com/mirror.kakao.com/g' -i.bak /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-virtualenv gunicorn3

# Setup flask application
RUN mkdir -p /deploy/app
COPY gunicorn_config.py /deploy/gunicorn_config.py
COPY app /deploy/app
RUN sed -i -e "s/@@BASE_DOMAIN@@/$base_domain/g" /deploy/app/hello.py && \
    sed -i -e "s/@@FIRST_SUBDOMAIN@@/$first_subdomain/g" /deploy/app/hello.py && \
    sed -i -e "s/@@SECOND_SUBDOMAIN@@/$second_subdomain/g" /deploy/app/hello.py
RUN python3 -m pip install -r /deploy/app/requirements.txt
RUN python3 -m pip install --upgrade psutil
WORKDIR /deploy/app

EXPOSE 8080

# Start gunicorn
CMD ["/usr/bin/gunicorn3", "--config", "/deploy/gunicorn_config.py", "hello:app"]
