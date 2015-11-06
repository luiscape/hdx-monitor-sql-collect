#!/bin/bash

#
# Deploying virtual environment.
#
pyvenv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

#
# Setting up database.
#
python configure.py
