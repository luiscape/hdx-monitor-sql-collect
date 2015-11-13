#!/bin/bash

#
# Starting rqinfo for checking
# statistis in the terminal.
#
source venv/bin/activate
rqinfo --url=$REDIS_PORT_6379_TCP_ADDR:6379
