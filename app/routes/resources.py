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
from app.functions.manage_queue import getStatus
from app.functions.fetch_store import fetchAndStore

ckan = CKAN().init()
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
    key = 'resources'
    status = getStatus(key)
    queue = Queue(connection=Redis(), name=key)
    objects = ckan.action.package_list()
    if status['empty']:
      for object in objects:
        job = queue.enqueue(fetchAndStore, key, object)

    response = {
        'success': True,
        'message': 'Computing resource information. {n} before finished.'.format(n=status['count']),
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
