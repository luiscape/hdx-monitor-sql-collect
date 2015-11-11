###################################################
#                                                 #
#   HDX Monitor: analytics service. Service for   #
#   providing analytics for the HDX Monitor.      #
#                                                 #
###################################################

FROM ubuntu:latest

MAINTAINER Luis Capelo <capelo@un.org>

#
# Installing Python 3.5
#
RUN \
  apt-get update \
  && apt-get -y upgrade \
  && apt-get install -y software-properties-common build-essential libffi-dev libssl-dev \
  && add-apt-repository ppa:fkrull/deadsnakes \
  && apt-get -y install wget git screen \
  && apt-get -y install python3.5 python3.5-dev python-dev python-distribute python-pip python-virtualenv

#
# Clone app and install dependencies.
#
RUN \
  git clone http://github.com/luiscape/hdx-monitor-sql-collect \
  && cd hdx-monitor-sql-collect \
  && make setup

WORKDIR "/hdx-monitor-sql-collect"

EXPOSE 3000 9181

CMD ["make", "run"]
