#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Blueprint of the /status route.
This route will be registered in `server.py`.

'''
#
# Status endpoints.
#
import flask
import app.utilities.load as Load

config = Load.loadJSONFile('config/dev.json')
blueprint_status = flask.Blueprint('status', __name__)

@blueprint_status.route('/')
@blueprint_status.route('/status')
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
