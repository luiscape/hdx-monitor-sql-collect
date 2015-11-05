#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for testing the User class.

'''
import os
import unittest

from app.classes.user import User

class TestClassUser:
  '''
  Performs tests on the User class.

  '''
  def __init__(self):
    self.keys = [
        'about', 'apikey', 'display_name',
        'name', 'created', 'email_hash', 'email',
        'sysadmin', 'state', 'number_of_edits', 'fullname',
        'id', 'number_created_packages'
      ]

  def test_user_keys(self):
    '''
    classes.user:  Test that the User class returns the right keys.

    '''
    result = User('luiscape').info()

    for key in self.keys:
      assert key in result.keys()
