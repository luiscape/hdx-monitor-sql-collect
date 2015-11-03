#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for testing the propmt formatter `item`.

'''

import os
import unittest
import app.utilities.item as Item

class TestUtilitiesItem:
  '''
  Unit tests for the item prompt formatter.

  '''

  def __init__(self):
    self.cases = ['warn', 'error', 'bullet', 'success']

  def test_type(self):
    '''
    utilities.item:  Test for the type of configuration files.

    '''
    for t in self.cases:
      result = Item.item(t)
      assert type(result) == type(u'')

