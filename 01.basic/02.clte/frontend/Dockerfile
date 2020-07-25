FROM ubuntu:bionic
ENV HAPROXY_UID haproxy
ENV HAPROXY_GID haproxy
ENV HAPROXY_VERSION 1.9.10
#WORKDIR /tmp/haproxy
#ADD ./haproxy-1.9.10/ /tmp/haproxy
ADD ./zairo.patch /tmp/zairo.patch

RUN sed -re 's/([a-z]{2}.)?archive.ubuntu.com/mirror.kakao.com/g' -e 's/security.ubuntu.com/mirror.kakao.com/g' -i.bak /etc/apt/sources.list
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates patch && \
    curl -fSL https://www.haproxy.org/download/1.9/src/haproxy-$HAPROXY_VERSION.tar.gz -o /tmp/haproxy-$HAPROXY_VERSION.tar.gz && \
    tar -zxC /tmp/ -f /tmp/haproxy-$HAPROXY_VERSION.tar.gz && \
    cd /tmp && \
    patch -p0 < zairo.patch && \
    apt-get install -y --no-install-recommends libssl1.0.0 zlib1g "libpcre2-*" liblua5.3-0 tar curl socat && \
    apt-get install -y --no-install-recommends gcc make libc6-dev libssl-dev libpcre3-dev zlib1g-dev liblua5.3-dev && \
    groupadd "$HAPROXY_GID" && \
    useradd -g "$HAPROXY_GID" "$HAPROXY_UID" && \
    make -C /tmp/haproxy-$HAPROXY_VERSION -j"$(nproc)" TARGET=linux2628 CPU=generic USE_PCRE2=1 USE_PCRE2_JIT=1 USE_REGPARM=1 USE_OPENSSL=1 \
                            USE_ZLIB=1 USE_TFO=1 USE_LINUX_TPROXY=1 USE_LUA=1 USE_GETADDRINFO=1 \
                            all && \
    make -C /tmp/haproxy-$HAPROXY_VERSION TARGET=linux2628 install-bin install-man && \
    ln -s /usr/local/sbin/haproxy /usr/sbin/haproxy && \
    mkdir -p /var/lib/haproxy && \
    chown "$HAPROXY_UID:$HAPROXY_GID" /var/lib/haproxy && \
    mkdir -p /usr/local/etc/haproxy && \
    ln -s /usr/local/etc/haproxy /etc/haproxy && \
    cp -R /tmp/haproxy-$HAPROXY_VERSION/examples/errorfiles /usr/local/etc/haproxy/errors && \
    rm -rf /tmp/haproxy-$HAPROXY_VERSION && \
    apt-get purge -y --auto-remove gcc make libc6-dev libssl-dev libpcre2-dev zlib1g-dev liblua5.3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY haproxy.cfg /usr/local/etc/haproxy
EXPOSE 1080
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]
