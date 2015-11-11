#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Blueprint of the /users route.
This route will be registered in `server.py`.

'''
#
# Status endpoints.
#
import flask
import app.utilities.load as Load

from rq import Queue
from redis import Redis

from app.classes.ckan import CKAN
from app.functions.manage_queue import getStatus
from app.functions.fetch_store import fetchAndStore

ckan = CKAN().init()
blueprint_users = flask.Blueprint('users', __name__)

@blueprint_users.route('/users')
def computeUsers():
    '''
    Computes information about all users from a
    CKAN instance.

    '''
    key = 'users'
    status = getStatus(key)
    queue = Queue(connection=Redis(), name=key)
    objects = ckan.action.user_list()
    if status['empty']:
      for object in objects:
        job = queue.enqueue(fetchAndStore, key, object['id'])

    response = {
        'success': True,
        'message': 'Computing user information. {n} before finished.'.format(n=status['count']),
        'endpoint': key,
        'time': None,
        'ETA': None,
        'computations': {
          'total': len(objects),
          'completed': len(objects) - status['count'],
          'queued': status['count'],
          'progress': round(((len(objects) - status['count']) / len(objects)) * 100, 2)
        }
      }

    return flask.jsonify(**response)
