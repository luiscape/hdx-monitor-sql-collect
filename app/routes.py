#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Flask application routes.

'''
import flask
import app.utilities.load as Load

from rq import Queue
from redis import Redis

from app.classes.ckan import CKAN
from app.functions.fetch_class_data import fetchClassData

from routes.status import blueprint_status
from routes.status import blueprint_datasets
from routes.status import blueprint_countries
from routes.status import blueprint_revisions
from routes.status import blueprint_gallery_items

def defineApplicationRoutes(app, config=None):
  '''
  Defines applicaton routes.

  '''
  ckan = CKAN().init()
  config = Load.loadJSONFile('config/dev.json')

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
