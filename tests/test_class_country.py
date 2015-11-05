#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for testing the Country class.

'''
import os
import unittest

from app.classes.country import Country

class TestClassCountry:
  '''
  Performs tests on the Country calss.

  '''
  def __init__(self):
    self.keys = [
        'users','display_name','description',
        'image_display_url','package_count',
        'created','name','is_organization',
        'title','revision_id','num_followers','id'
      ]

  def test_country_keys(self):
    '''
    classes.country:  Test that the Country classe returns the right keys.

    '''
    result = Country('irq').info()

    for key in self.keys:
      assert key in result.keys()
