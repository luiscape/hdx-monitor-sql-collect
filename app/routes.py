#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Flask application routes.

'''
import flask
import app.utilities.load as Load

from rq import Queue
from redis import Redis

from app.classes.user import User
from app.classes.ckan import CKAN
from app.classes.country import Country
from app.classes.dataset import Dataset
from app.classes.revision import Revision
from app.classes.resource import Resource
from app.classes.gallery_item import GalleryItem

queue = Queue(connection=Redis())

def defineApplicationRoutes(app, config=None):
  '''
  Defines applicaton routes.

  '''
  ckan = CKAN().init()
  config = Load.loadJSONFile('config/dev.json')

  #
  # Status endpoints.
  #
  @app.route('/')
  @app.route('/status')
  def statusPage():
    '''
    Serves a JSON object with the current status,
    version number, and description of the application.

    '''
    result = {
      'online': True,
      'version': config['version'],
      'ckan': config['ckan']['url'],
      'maintainer': config['maintainer'],
      'repository': config['repository'],
      'description': config['description']
    }
    return flask.jsonify(**result)

  #
  # Computing endpoints.
  #
  @app.route('/users')
  def computeUsers():
    '''
    Computes information about all users of a
    CKAN instance.

    '''
    response = ckan.action.user_list()

    return flask.jsonify(**response)

  @app.route('/countries')
  def computeCountries():
    '''
    Computes information about all countries of a
    CKAN instance.

    '''
    countries = ckan.action.group_list()
    for country in countries:
      job = queue.enqueue(Country.info, country)

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


  @app.route('/dataset')
  def computeDatasets():
    '''
    Computes information about all datasets of a
    CKAN instance.

    '''
    CKAN = 'https://data.hdx.rwlabs.org/api/3/action'
    r = requests.get('{CKAN}/user_list'.format(CKAN))
    datasets = r.json().result()

    for dataset in datasets:
      job = q.enqueue(utils.update, endpoint, **opts)
      # result_url = '%s/result/%s/' % (base, job.id)

      resp = {
            'id': job.id,
            'status': job.get_status()
          }

      return jsonify(**resp)

  @app.route('/organizations')
  def computeOrganizations():
    '''
    Computes information about all organizations of a
    CKAN instance.

    '''
    print('foo')

  @app.route('/resouces')
  def computeResources():
    '''
    Computes information about all resources of a
    CKAN instance.

    '''
    print('foo')

  @app.route('/revisions')
  def computeRevisions():
    '''
    Computes information about all revisions of a
    CKAN instance.

    '''
    print('foo')

  @app.route('/gallery_items')
  def computeGalleryItems():
    '''
    Computes information about all gallery items of a
    CKAN instance.

    '''
    print('foo')

  #
  # Helper endpoints
  #
  @app.route('/all')
  def computeAll():
    '''
    Computes information about all CKAN objects.

    '''
    print('foo')
