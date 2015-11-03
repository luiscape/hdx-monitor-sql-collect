#!/bin/bash

#
# Run tests with coverage.
#
source venv/bin/activate
nosetests --with-cov --cov-report term-missing -d -v
