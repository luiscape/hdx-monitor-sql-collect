#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Functions to start and configure the Flask
application. Loads routes from the routes.py
script.

'''
import flask

from app.classes.ckan import CKAN
from app.routes.users import blueprint_users
from app.routes.queues import blueprint_queues
from app.routes.status import blueprint_status
from app.routes.datasets import blueprint_datasets
from app.routes.countries import blueprint_countries
from app.routes.revisions import blueprint_revisions
from app.routes.resources import blueprint_resources
from app.routes.organizations import blueprint_organizations
from app.routes.gallery_items import blueprint_gallery_items

def createServer(database_uri, debug=False):
  '''
  Creates a Flask application as an object.
  '''

  app = flask.Flask(__name__)
  app.debug = debug
  app.host = '0.0.0.0'

  app.register_blueprint(blueprint_users)
  app.register_blueprint(blueprint_status)
  app.register_blueprint(blueprint_queues)
  app.register_blueprint(blueprint_datasets)
  app.register_blueprint(blueprint_countries)
  app.register_blueprint(blueprint_revisions)
  app.register_blueprint(blueprint_resources)
  app.register_blueprint(blueprint_organizations)
  app.register_blueprint(blueprint_gallery_items)

  return app
