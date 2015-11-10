#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Function to manage the Redis Queue. In summary
this function either

  (a) starts a new queue if no jobs are pending
  (b) fetches statistics from a running queue
  (c) cancels a queue and starts again

This function was designed to be called directly
by the routes so that the final user knows what
is the current status of the running queues.

'''
import flask

from rq import Queue
from redis import Redis

def getStatus(queue_id='default'):
  '''
  Gets status of queue.

  '''
  queue = Queue(connection=Redis(), name=queue_id)
  result = {
    'message': 'Queue `{name}` is not empty. {n} jobs are being processed.'.format(name=queue_id, n=queue.count),
    'empty': queue.is_empty(),
    'count': queue.count,
    'ids': queue.get_job_ids()
  }

  return result

def cleanQueue(queue_id='default'):
  '''
  Cleans specified queue.

  '''
  queue = Queue(connection=Redis(), name=queue_id)
  result = {
      'success': True,
      'message': 'Cleaned {n} jobs successfully from `{name}`.'.format(n=queue.empty(), name=queue_id)
    }
  return result
