#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Blueprint of the /resources route.
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
blueprint_resources = flask.Blueprint('resources', __name__)

@blueprint_resources.route('/resources')
def computeResources():
    '''
    Computes information about all resources from a
    CKAN instance.

    '''
    #
    # TODO: there aren't resource_list
    # method to list all resources from a
    # a CKAN instance.
    #
    # This route should not be registered
    # right now.
    #
    key = 'resource'
    objects = ckan.action.package_list()
    for object in objects:
      job = queue.enqueue(fetchAndStore, key, object['id'])

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
