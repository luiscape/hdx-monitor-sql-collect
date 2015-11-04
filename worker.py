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
QUEUES = ['high', 'normal', 'low']
REDIS_URL = 'redis://localhost:6379/1'

# REDIS_DB = 3
# REDIS_PORT = 6380
# REDIS_PASSWORD = 'very secret'
# REDIS_HOST = 'redis.example.com'
