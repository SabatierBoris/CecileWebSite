FROM debian:latest
MAINTAINER Boris SABATIER sabatier.boris@gmail.com

EXPOSE 80

RUN apt-get -y update
RUN apt-get -y upgrade

RUN apt-get -y install python3
RUN apt-get -y install python3-all-dev
RUN apt-get -y install python3-setuptools
RUN apt-get -y install libpq-dev
RUN apt-get -y install libjpeg-dev
RUN apt-get -y install zlib1g-dev
RUN apt-get -y install gcc
RUN apt-get -y install libfreetype6-dev

ENV APP_DIR /www
ADD . /www
WORKDIR /www

RUN python3 setup.py install
RUN python3 setup.py develop

ENTRYPOINT ["/www/runProd.sh"]
