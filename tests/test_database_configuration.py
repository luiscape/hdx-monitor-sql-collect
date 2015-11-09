#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for checking that the database
configuration is setup correctly.

'''

import os
import unittest
import app.utilities.load as Load

class TestDatabaseConfiguration(unittest.TestCase):
  '''
  Unit tests for the checking the database properties of
  the configuration files.

  '''
  def setUp(self):
    dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    self.folder = os.path.join(dir_name, 'config')
    self.files = [
        os.path.join(self.folder, 'dev.json'),
        os.path.join(self.folder, 'prod.json')
      ]

  def test_structure(self):
    '''
    database.configuration.file:  Test for the structure of configuration files.

    '''
    keys = ['name', 'primary_key', 'columns']
    for file in self.files:
      result = Load.loadJSONFile(file)
      for table in result['database']:
        for key in table.keys():
          self.assertIn(key, keys)


class TestTableConfiguration(unittest.TestCase):
  '''
  Unit tests for checking if the tables
  contain the right column names.

  '''
  def setUp(self):
    dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    self.folder = os.path.join(dir_name, 'config')
    self.files = [
        os.path.join(self.folder, 'dev.json'),
        os.path.join(self.folder, 'prod.json')
      ]
    self.tables = {
      'country': [
        'display_name','description','package_count',
        'created','name', 'title','revision_id',
        'num_followers','id'
      ],
      'dataset' : [
        'license_title', 'maintainer', 'package_creator',
        'private', 'dataset_date', 'num_tags', 'id',
        'metadata_created', 'indicator', 'methodology_other',
        'caveats', 'metadata_modified', 'author', 'author_email',
        'license_other', 'methodology', 'dataset_source',
        'license_id', 'num_resources', 'creator_user_id',
        'maintainer_email', 'name', 'notes', 'owner_org',
        'title', 'revision_id', 'tracking_summary_total',
        'tracking_summary_recent'
      ],
      'gallery_item': [
        'description','view_count','url',
        'title','image_url','type','id',
        'owner_id'
      ],
      'resource': [
        'resource_uploader','package_id','datastore_active',
        'id','description','format','tracking_summary_total',
        'last_modified','url_type','name','created',
        'url','revision_id', 'tracking_summary_recent'
      ],
      'revision': [
        'id', 'timestamp', 'message',
        'author', 'action_type'
      ],
      'user': [
        'about', 'display_name',
        'name', 'created', 'email_hash', 'email',
        'sysadmin', 'state', 'number_of_edits', 'fullname',
        'id', 'number_created_packages'
      ]
    }

  def test_column_names(self):
    '''
    database.configuration.tables:  Test that column names are correct.

    '''
    for file in self.files:
      database = Load.loadJSONFile(file)['database']
      for table in database:
        #
        # Don't test the 'test' table.
        #
        if table['name'] == 'test':
          continue
        else:
          for column in table['columns']:
            self.assertIn(column['field_name'], self.tables.get(table['name']))
