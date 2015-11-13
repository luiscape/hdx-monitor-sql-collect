#!/bin/bash

#
# Starting the RQ
# dashboard.
#
source venv/bin/activate
screen -S dashboard -d -m -L rq-dashboard --redis_url=redis://$REDIS_PORT_6379_TCP_ADDR:6379
