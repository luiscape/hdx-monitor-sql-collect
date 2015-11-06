#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Blueprint of the /countries route.
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
blueprint_countries = flask.Blueprint('countries', __name__)

@blueprint_countries.route('/countries')
def computeCountries():
    '''
    Computes information about all countries of a
    CKAN instance.

    '''
    countries = ckan.action.group_list()
    for country in countries:
      job = queue.enqueue(fetchAndStore, 'country', country)

    response = {
        'success': True,
        'message': 'Computing countries information.',
        'endpoint': 'countries',
        'time': None,
        'ETA': '1 hour and 30 minutes',
        'computations': {
          'total': len(countries),
          'completed': None,
          'failed': None,
          'queued': None,
          'progress': None
        }
      }

    return flask.jsonify(**response)
