#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Blueprint of the /organizations route.
This route will be registered in `server.py`.

'''
import flask
import app.utilities.load as Load

from rq import Queue
from redis import Redis

from app.classes.ckan import CKAN
from app.functions.manage_queue import getStatus
from app.functions.fetch_store import fetchAndStore

ckan = CKAN().init()
blueprint_organizations = flask.Blueprint('organizations', __name__)

@blueprint_organizations.route('/organizations')
def computeOrganizations():
    '''
    Computes information about all organizations of a
    CKAN instance.

    '''
    key = 'organizations'
    status = getStatus(key)
    queue = Queue(connection=Redis(), name=key)
    objects = ckan.action.organization_list()
    if status['empty']:
      for object in objects:
        job = queue.enqueue(fetchAndStore, key, object)

    response = {
        'success': True,
        'message': 'Computing organization information. {n} before finished.'.format(n=status['count']),
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
