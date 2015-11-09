#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for testing the Dataset class.

'''
import os
import unittest

from app.classes.dataset import Dataset

class TestClassDataset(unittest.TestCase):
  '''
  Performs tests on the Dataset calss.

  '''
  def setUp(self):
    self.keys = [
      'license_title', 'maintainer', 'package_creator',
      'private', 'dataset_date', 'num_tags', 'id',
      'metadata_created', 'indicator', 'methodology_other',
      'caveats', 'metadata_modified', 'author', 'author_email',
      'license_other', 'methodology', 'dataset_source',
      'license_id', 'num_resources', 'creator_user_id',
      'maintainer_email', 'name', 'notes', 'owner_org',
      'title', 'revision_id', 'tracking_summary_total',
      'tracking_summary_recent'
    ]

  def test_dataset_keys(self):
    '''
    classes.dataset:  Test that the Dataset classe returns the right keys.

    '''
    result = Dataset('ebola-cases-2014').info()

    for key in self.keys:
      self.assertIn(key, result.keys())
