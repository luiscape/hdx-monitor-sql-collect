#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for testing the Revision class.
The `action_type` key was added.

'''
import os
import unittest

from app.classes.revision import Revision

class TestClassRevision(unittest.TestCase):
  '''
  Performs tests on the Revision class.

  '''
  def __init__(self):
    self.keys = [
        'id', 'timestamp', 'message',
        'author', 'action_type'
      ]

  def test_revision_keys(self):
    '''
    classes.revision:  Test that the Revision class returns the right keys.

    '''
    result = Revision('b1e6f54d-d086-4c03-9739-84ae400e5aa1').info()

    for key in self.keys:
      self.assertIn(key, result.keys())
