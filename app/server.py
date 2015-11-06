#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Functions to start and configure the Flask
application. Loads routes from the routes.py
script.

'''
import flask

# from app.routes import defineApplicationRoutes
from app.routes.status import blueprint_status
from app.routes.countries import blueprint_countries

def createServer(database_uri, debug=False):
  '''
  Creates a Flask application as a class instance.
  '''

  app = flask.Flask(__name__)
  app.debug = debug
  app.host = '0.0.0.0'

  app.register_blueprint(blueprint_status)
  app.register_blueprint(blueprint_countries)

  # defineApplicationRoutes(app)

  return app
