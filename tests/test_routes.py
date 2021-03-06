#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Integration tests for testing the application
HTTP routes and methods.

'''
import json
import flask
import unittest
import app.server as Server

class Generic(unittest.TestCase):
  '''
  Set of generic tests.

  '''
  def setUp(self, object):
    self.object = object

  def keys(self):
    '''
    Generic test for expected default keys.

    '''
    keys = ['success', 'message', 'endpoint', 'time', 'ETA', 'computations']
    for key in self.object.keys():
      self.assertIn(key, keys)

  def computations(self):
    '''
    Generic test for expected computation keys.

    '''
    computation_keys = ['total', 'completed', 'failed', 'queued', 'progress']
    for key in self.object['computations']:
      self.assertIn(key, computation_keys)

  def types(self):
    '''
    Generic test for the types of data.

    '''
    types = {
      'online': bool,
      'message': str,
      'endpoint': str,
      'time': str,
      'ETA': str,
      'computations': {
        'total': int,
        'completed': int,
        'failed': int,
        'queued': int,
        'progress': float
      }
    }
    for key in self.object.keys():
      self.assertIs(type(self.object.get(key)), types[key])
      if type(key) == type({}):
        for k in key:
          self.assertIs(type(self.object['computations'].get(key)), types['computations'][k])


class TestRoutes(unittest.TestCase):
  '''
  Tests for all routes and methods.

  '''
  def setUp(self):
    self.app = Server.createServer('test', debug=False)
    self.client = self.app.test_client()

  #
  # /status
  #
  def test_status_type(self):
    '''
    routes.status:  /status endpoint returns a JSON object.

    '''
    response = self.client.get('/status')
    result = json.loads(response.data.decode('utf8'))
    self.assertIs(type(result), type({}))

  def test_status_object(self):
    '''
    routes.status:  /status endpoint returns a complete object.

    '''
    response = self.client.get('/status')
    result = json.loads(response.data.decode('utf8'))

    keys = ['online', 'version', 'description', 'repository', 'maintainer', 'ckan']
    for key in result.keys():
      self.assertIn(key, keys)

  # #
  # # /users
  # #
  # def test_users_type(self):
  #   '''
  #   routes:  /users endpoint returns a JSON object.

  #   '''
  #   response = self.client.get('/users')
  #   result = json.loads(response.data.decode('utf8'))
  #   assert type(result) == type({})

  # def test_users_object(self):
  #   '''
  #   routes:  /users endpoint returns a complete object.

  #   '''
  #   response = self.client.get('/users')
  #   result = json.loads(response.data.decode('utf8'))

  #   generic = Generic(result)
  #   generic.keys()
  #   generic.types()
  #   generic.computations()

  #
  # /revisions
  #
  def test_revisions_type(self):
    '''
    routes.revisions:  /revisions endpoint returns a JSON object.

    '''
    response = self.client.get('/revisions')
    result = json.loads(response.data.decode('utf8'))
    self.assertIs(type(result) == type({}))

  def test_revisions_object(self):
    '''
    routes.revisions:  /revisions endpoint returns a complete object.

    '''
    response = self.client.get('/revisions')
    result = json.loads(response.data.decode('utf8'))

    generic = Generic(result)
    generic.keys()
    generic.types()
    generic.computations()

  #
  # /datasets
  #
  def test_datasets_type(self):
    '''
    routes.datasets:  /datasets endpoint returns a JSON object.

    '''
    response = self.client.get('/datasets')
    result = json.loads(response.data.decode('utf8'))
    self.assertIs(type(result), type({}))

  def test_datasets_object(self):
    '''
    routes.datasets:  /datasets endpoint returns a complete object.

    '''
    response = self.client.get('/datasets')
    result = json.loads(response.data.decode('utf8'))

    generic = Generic(result)
    generic.keys()
    generic.types()
    generic.computations()

  #
  # /resources
  #
  def test_resources_type(self):
    '''
    routes.resources:  /resources endpoint returns a JSON object.

    '''
    response = self.client.get('/resources')
    result = json.loads(response.data.decode('utf8'))
    self.assertIs(type(result), type({}))

  def test_resources_object(self):
    '''
    routes.resources:  /resources endpoint returns a complete object.

    '''
    response = self.client.get('/resources')
    result = json.loads(response.data.decode('utf8'))

    generic = Generic(result)
    generic.keys()
    generic.types()
    generic.computations()

  #
  # /countries
  #
  def test_countries_type(self):
    '''
    routes.countries:  /countries endpoint returns a JSON object.

    '''
    response = self.client.get('/countries')
    result = json.loads(response.data.decode('utf8'))
    self.assertIs(type(result), type({}))

  def test_countries_object(self):
    '''
    routes.countries:  /countries endpoint returns a complete object.

    '''
    response = self.client.get('/countries')
    result = json.loads(response.data.decode('utf8'))

    generic = Generic(result)
    generic.keys()
    generic.types()
    generic.computations()

  #
  # /gallery_items
  #
  def test_gallery_items_type(self):
    '''
    routes:.gallery_items  /gallery_items endpoint returns a JSON object.

    '''
    response = self.client.get('/gallery_items')
    result = json.loads(response.data.decode('utf8'))
    self.assertIs(type(result), type({}))

  def test_gallery_items_object(self):
    '''
    routes.gallery_items:  /gallery_items endpoint returns a complete object.

    '''
    response = self.client.get('/gallery_items')
    result = json.loads(response.data.decode('utf8'))

    generic = Generic(result)
    generic.keys()
    generic.types()
    generic.computations()

  #
  # /organizations
  #
  def test_organizations_type(self):
    '''
    routes.organizations:  /organizations endpoint returns a JSON object.

    '''
    response = self.client.get('/organizations')
    result = json.loads(response.data.decode('utf8'))
    self.assertIs(type(result), type({}))

  def test_organizations_object(self):
    '''
    routes.organizations:  /organizations endpoint returns a complete object.

    '''
    response = self.client.get('/organizations')
    result = json.loads(response.data.decode('utf8'))

    generic = Generic(result)
    generic.keys()
    generic.types()
    generic.computations()
