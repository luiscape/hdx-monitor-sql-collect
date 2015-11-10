#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Blueprint of the /countries route.
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
queue = Queue(connection=Redis())
blueprint_countries = flask.Blueprint('countries', __name__)

@blueprint_countries.route('/countries')
def computeCountries():
    '''
    Computes information about all countries of a
    CKAN instance.

    '''
    status = getStatus('default')
    countries = ckan.action.group_list()
    if status['empty']:
      for country in countries:
        job = queue.enqueue(fetchAndStore, 'country', country)

    response = {
        'success': True,
        'message': 'Computing countries information.',
        'endpoint': 'countries',
        'time': None,
        'ETA': None,
        'computations': {
          'total': len(countries),
          'completed': len(countries) - status['count'],
          'queued': status['count'],
          'progress': round(((len(countries) - status['count']) / len(countries)) * 100, 2)
        }
      }

    return flask.jsonify(**response)
