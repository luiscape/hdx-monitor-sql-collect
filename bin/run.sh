#!/bin/bash

#
# Start workers.
#
for i in {1..4}
do
  echo "Starting worker $i."
  make worker
done
screen -ls

#
# Start RQ-Dashboard.
#
echo "Starting RQ Dashboard."
make dashboard

#
# Start Flask server.
#
source venv/bin/activate
python run.py
