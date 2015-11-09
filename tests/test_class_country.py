#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for testing the Country class.

'''
import os
import unittest

from app.classes.country import Country

class TestClassCountry(unittest.TestCase):
  '''
  Performs tests on the Country calss.

  '''
  def setUp(self):
    self.keys = [
        'display_name','description','package_count',
        'created','name', 'title','revision_id',
        'num_followers','id'
      ]

  def test_country_keys(self):
    '''
    classes.country:  Test that the Country class returns the right keys.

    '''
    result = Country('irq').info()

    for key in self.keys:
      self.assertIn(key, result.keys())
