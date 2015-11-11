#!/bin/bash

#
# Start worker for interfacing with Redis.
#
source venv/bin/activate
screen -S worker -d -m -L rqworker -c worker
