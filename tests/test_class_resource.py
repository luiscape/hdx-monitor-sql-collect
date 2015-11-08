#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for testing the Resource class.

'''
import os
import unittest

from app.classes.resource import Resource

class TestClassResource(unittest.TestCase):
  '''
  Performs tests on the Resource calss.

  '''
  def __init__(self):
    self.keys = [
        'resource_uploader','package_id','datastore_active',
        'id','description','format', 'last_modified','url_type',
        'name','created', 'url','revision_id', 'tracking_summary_total',
        'tracking_summary_recent'
      ]


  def test_resource_keys(self):
    '''
    classes.resource:  Test that the Resource classe returns the right keys.

    '''
    result = Resource('c59b5722-ca4b-41ca-a446-472d6d824d01').info()

    for key in self.keys:
      self.assertIn(key, result.keys())
