#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Flask application routes.

'''
import flask
import app.utilities.load as Load

def defineRoutes(app):
  '''
  Defines applicaton routes.

  '''
  @app.route('/')
  @app.route('/status')
  def statusPage():
    config = Load.loadJSONFile('config/dev.json')
    out = {
      'online': True,
      'version': config['version'],
      'description': config['description'],
      'repository': config['repository']
    }
    return flask.jsonify(**out)

  # @app.routes('/users'):

