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


class TestRoutes:
  '''
  Tests for all routes and methods.

  '''
  def __init__(self):
    self.app = Server.createServer('test', debug=False)
    self.client = self.app.test_client()

  def test_status_type(self):
    '''
    routes.status:  test the /status endpoint returns a JSON object.

    '''
    response = self.client.get('/status')
    result = json.loads(response.data.decode('utf8'))
    assert type(result) == type({})

  def test_status_object(self):
    '''
    routes.status:  test the /status endpoint returns a complete object.

    '''
    response = self.client.get('/status')
    result = json.loads(response.data.decode('utf8'))

    keys = ['online', 'version', 'description', 'repository', 'maintainer']
    for key in result.keys():
      assert key in keys
