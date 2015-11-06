#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for testing data is stored in
the database correctly.

'''
import os
import unittest
import psycopg2

from app.functions.store_data import storeData

class TestFunctionClassData(unittest.TestCase):
  '''
  Perfroms tests on the data storage function.

  '''
  def setUp(self):
    self.data = [
      { 'id': 'test-id', 'name': 'test-name', 'created': 'test-timestamp' },
      { 'id': 'test-id', 'name': 'test-name', 'created': 'test-timestamp' }
    ]
    self.conn = psycopg2.connect(
        host=os.environ.get('POSTGRES_PORT_5432_TCP_ADDR'),
        dbname='metabase',
        user='metabase',
        password='metabase'
      )
    self.cur = self.conn.cursor()


  def tearDown(self):
    statement = 'DELETE FROM test'

    self.cur.execute(statement)
    self.conn.commit()

    self.cur.close()
    self.conn.close()

  def test_data_storage_doesnt_fail(self):
    '''
    functions.store_data_insert:  Test that the data storage inserts data properly.

    '''
    storeData(self.data, 'test')


  def test_update_works(self):
    '''
    functions.store_data_update:  Test that the data storage updates data properly.

    '''
    storeData(self.data, 'test')
