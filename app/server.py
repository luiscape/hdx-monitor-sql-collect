#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Functions to start and configure the Flask
application. Loads routes from the routes.py
script.

'''
import flask
import app.utilities.load as Load

from rq import Queue
from redis import Redis

from app.classes.ckan import CKAN
from app.functions.fetch_class_data import fetchClassData

from app.routes.status import blueprint_status
from app.routes.datasets import blueprint_datasets
from app.routes.countries import blueprint_countries
from app.routes.revisions import blueprint_revisions
from app.routes.gallery_items import blueprint_gallery_items

def createServer(database_uri, debug=False):
  '''
  Creates a Flask application as a class instance.
  '''

  app = flask.Flask(__name__)
  app.debug = debug
  app.host = '0.0.0.0'

  app.register_blueprint(blueprint_status)
  app.register_blueprint(blueprint_datasets)
  app.register_blueprint(blueprint_countries)
  app.register_blueprint(blueprint_revisions)
  app.register_blueprint(blueprint_gallery_items)

  #
  # Helper endpoints
  #
  @app.route('/all')
  def computeAll():
    '''
    Computes information about all CKAN objects.

    '''
    print('foo')

  return app
