FROM python:alpine

RUN apk update && \
    apk add \
      curl \
      shadow \
      unzip && \
    curl -LO https://releases.hashicorp.com/packer/1.7.4/packer_1.7.4_linux_amd64.zip && \
    unzip packer*.zip && \
    useradd packer && \
    echo "packer:packer" | /usr/sbin/chpasswd && \
    mkdir -p /home/packer && \
    mkdir -p /usr/src/python_packer && \
    chown -R packer:packer /home/packer && \
    chown -R packer:packer /usr/src/python_packer

COPY . /usr/src/python_packer
WORKDIR /usr/src/python_packer

USER packer

