#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Functions to start and configure the Flask
application. Loads routes from the routes.py
script.

'''
import flask

from app.routes import defineApplicationRoutes

def createServer(database_uri, debug=False):
  '''
  Creates a Flask application as a class instance.
  '''

  app = flask.Flask(__name__)
  app.debug = debug
  app.host = '0.0.0.0'

  defineApplicationRoutes(app)

  return app
