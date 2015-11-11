#!/bin/bash

#
# Starting the RQ
# dashboard.
#
source venv/bin/activate
screen -S worker -d -m -L rq-dashboard
