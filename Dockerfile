###################################################
#                                                 #
#   HDX Monitor: analytics service. Service for   #
#   providing analytics for the HDX Monitor.      #
#                                                 #
###################################################

FROM python:3.5

MAINTAINER Luis Capelo <capelo@un.org>

#
# Making sure terminal
# uses utf-8.
#
RUN \
  export LC_ALL=en_US.UTF-8 \
  && export LANG=en_US.UTF-8 \
  && export LANGUAGE=en_US.UTF-8

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
