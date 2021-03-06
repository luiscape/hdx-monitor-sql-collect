#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Blueprint of the /datasets route.
This route will be registered in `server.py`.

'''
import os
import flask
import app.utilities.load as Load

from rq import Queue
from redis import Redis

from app.classes.ckan import CKAN
from app.functions.manage_queue import getStatus
from app.functions.fetch_store import fetchAndStore

ckan = CKAN().init()
REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR')
blueprint_datasets = flask.Blueprint('datasets', __name__)

@blueprint_datasets.route('/datasets')
def computeDatasets():
    '''
    Computes information about all datasets from a
    CKAN instance.

    '''
    key = 'datasets'
    status = getStatus(key)
    queue = Queue(connection=Redis(host=REDIS_HOST), name=key)
    objects = ckan.action.package_list()
    if status['empty']:
      for object in objects:
        job = queue.enqueue(fetchAndStore, key, object)

    response = {
        'success': True,
        'message': 'Computing datasets information. {n} before finished.'.format(n=status['count']),
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
