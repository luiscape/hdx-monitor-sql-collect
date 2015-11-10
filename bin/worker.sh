#!/bin/bash

#
# Start worker for interfacing with Redis.
#
source venv/bin/activate
python -V
rqworker -c worker
