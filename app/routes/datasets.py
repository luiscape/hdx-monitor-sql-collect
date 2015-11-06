#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Blueprint of the /datasets route.
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
from app.functions.fetch_store import fetchAndStore

ckan = CKAN().init()
queue = Queue(connection=Redis())
blueprint_datasets = flask.Blueprint('datasets', __name__)

@blueprint_datasets.route('/datasets')
def computeDatasets():
    '''
    Computes information about all datasets from a
    CKAN instance.

    '''
    key = 'dataset'
    objects = ckan.action.package_list()
    for object in objects:
      job = queue.enqueue(fetchAndStore, key, object)

    response = {
        'success': True,
        'message': 'Computing users information.',
        'endpoint': key,
        'time': None,
        'ETA': '1 hour and 30 minutes',
        'computations': {
          'total': len(objects),
          'completed': None,
          'failed': None,
          'queued': None,
          'progress': None
        }
      }

    return flask.jsonify(**response)
