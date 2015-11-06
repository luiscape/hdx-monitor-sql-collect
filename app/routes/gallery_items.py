#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Blueprint of the /gallery_items route.
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
blueprint_gallery_items = flask.Blueprint('gallery_items', __name__)

@blueprint_gallery_items.route('/gallery_items')
def computeGalleryItems():
    '''
    Computes information about all gallery items from a
    CKAN instance.

    '''
    key = 'gallery_item'
    objects = ckan.action.related_list()
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
