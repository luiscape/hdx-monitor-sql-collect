#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Blueprint of the /queue route. Here are included
routes to manage the differnt job queues. This
route will be registered in `server.py`.

'''
#
# Status endpoints.
#
import flask

from app.functions.manage_queue import getStatus, cleanQueue

blueprint_queues = flask.Blueprint('queues', __name__)

@blueprint_queues.route('/queue/<queue_id>')
@blueprint_queues.route('/queue')
def queue(queue_id='default'):
  '''
  Fetches the number of jobs being
  processed at a determinate queue endpoint.
  '''
  result = getStatus(queue_id)
  return flask.jsonify(**result)

@blueprint_queues.route('/queue/clean/<queue_id>')
def clean(queue_id='default'):
  '''
  Cleans a queue endpoint.

  '''
  result = cleanQueue(queue_id)
  return flask.jsonify(**result)
