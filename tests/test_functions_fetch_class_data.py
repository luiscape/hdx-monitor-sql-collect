#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for checking test data is
fetched correctly.

'''
import unittest
import app.utilities.load as Load

from app.functions.fetch_class_data import fetchClassData, _fields

config = Load.loadJSONFile('config/dev.json')

class TestFunctionFetchClassData(unittest.TestCase):
  '''
  Performs test for checking function to retrieve
  a specific class data.

  '''
  def setUp(self):
    self.classes = [
      { 'class': 'country', 'data': 'irq' },
      { 'class': 'dataset', 'data': 'ebola-cases-2014' },
      { 'class': 'gallery_item', 'data': '753ccf05-872f-4c8d-9cc2-8e562f6fc1d5' },
      { 'class': 'resource', 'data': 'c59b5722-ca4b-41ca-a446-472d6d824d01' },
      { 'class': 'revision', 'data': 'b1e6f54d-d086-4c03-9739-84ae400e5aa1' },
      { 'class': 'user', 'data': 'luiscape' }
    ]

  def test_object_type(self):
    '''
    functions.class_type:  Tests that class data is a dictionary object.

    '''
    for c in self.classes:
      result = fetchClassData(c['class'], c['data'])
      self.assertIs(type(result), type({}))


  def test_object_keys(self):
    '''
    functions.class_data:  Test for class data keys.

    '''
    for c in self.classes:
      keys = _fields(config, c['class'])
      result = fetchClassData(c['class'], c['data'])
      for key in keys:
        self.assertIn(key, result.keys())
