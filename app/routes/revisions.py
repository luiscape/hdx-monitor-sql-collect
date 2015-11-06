#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Blueprint of the /revisions route.
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
blueprint_revisions = flask.Blueprint('revisions', __name__)

@blueprint_revisions.route('/revisions')
def computeRevisions():
    '''
    Computes information about all revisions from a
    CKAN instance.

    '''
    key = 'revision'
    objects = ckan.action.revision_list()
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
