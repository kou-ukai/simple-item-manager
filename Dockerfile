FROM python:3.10-slim

# git
RUN apt update -y && apt upgrade -y && apt-get install -y curl git

# node
RUN curl -fsSL https://deb.nodesource.com/setup_17.x | bash - \
  && apt-get install -y nodejs

WORKDIR /workspace