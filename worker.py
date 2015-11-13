#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Settings for the RQ worker. It contains:

  - REDIS_URL: Redis connection string.

or

  - REDIS_HOST: host name.
  - REDIS_PORT: port number.
  - REDIS_DB: database number.
  - REDIS_PASSWORD: database password.

The queues can also be configured:

  - QUEUES: names of the queues.


'''
import os

REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR')
REDIS_URL = 'redis://{host}:6379/0'.format(host=REDIS_HOST)
QUEUES = [
  'users',
  'helpers',
  'resouces',
  'datasets',
  'countries',
  'revisions',
  'resources',
  'organizations',
  'gallery_items'
  ]

# REDIS_DB = 3
# REDIS_PORT = 6380
# REDIS_PASSWORD = 'very secret'
# REDIS_HOST = 'redis.example.com'
