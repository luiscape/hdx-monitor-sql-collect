#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for the loading of configuration files.
Tests for the structure of configuration files and
the output of functions that load them.

'''

import os
import unittest
import app.utilities.load as Load

class TestUtilityLoad(unittest.TestCase):
  '''
  Unit tests for the loading of configuration files.

  '''

  def __init__(self):
    dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    self.folder = os.path.join(dir_name, 'config')
    self.files = [
        os.path.join(self.folder, 'dev.json'),
        os.path.join(self.folder, 'prod.json')
      ]

  def test_type(self):
    '''
    utilities.load:  Test for the type of configuration files.

    '''
    for file in self.files:
      result = Load.loadJSONFile(file)
      self.assertIs(type(result), type({}))

  def test_structure(self):
    '''
    utilities.load:  Test for the structure of configuration files.

    '''
    keys = ['version', 'description', 'repository', 'maintainer', 'ckan', 'database']
    for file in self.files:
      result = Load.loadJSONFile(file)
      for key in result.keys():
        self.assertIn(key, keys)
