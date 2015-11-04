FROM debian:latest
MAINTAINER Boris SABATIER sabatier.boris@gmail.com

EXPOSE 8080


RUN apt-get update
RUN apt-get upgrade

RUN apt-get install -y python3
RUN apt-get install -y python3-all-dev
RUN apt-get install -y python3-setuptools
RUN apt-get install -y libjpeg-dev
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y gcc

ENV APP_DIR /www
ADD . /www
WORKDIR /www

RUN python3 setup.py install

ENTRYPOINT ["pserve"]
CMD ["pyramidapp/config/production.ini"]
