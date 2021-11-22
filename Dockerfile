FROM python:3.10-alpine

RUN mkdir -p /usr/src/server

COPY ./server /usr/src/server

WORKDIR /usr/src/server
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt update -y && apt upgrade -y && apt-get install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_17.x | bash -
  && apt-get install -y nodejs npm

WORKDIR /usr/src