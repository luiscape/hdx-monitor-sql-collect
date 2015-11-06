#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Function that stores records from a Python
dictionary into a PostgreSQL database table.
It will perform an insert if the record
doesn't exist and an update if it exists.

'''
import os
import psycopg2

from app.utilities.item import item
from app.utilities.load import loadJSONFile

HOST_DATABASE = os.environ.get('POSTGRES_PORT_5432_TCP_ADDR')

def storeData(data, table):
  '''
  Store records in a PostgreSQL database.

  '''
  #
  # TODO: add environment variables
  # to these default values.
  #
  conn = psycopg2.connect(host=HOST_DATABASE, dbname='metabase', user='metabase', password='metabase')
  cur = conn.cursor()

  #
  # Check no NULL values are passed.
  #
  for key in data.keys():
    if data.get(key) is None:
      data.pop(key)

  #
  # Using `upsert` statement newly available
  # on PostgreSQL 9.5. We are using a beta version
  # of the database.
  #
  columns = 'INSERT INTO {table} ({columns}) '.format(table=table, columns=",".join(data.keys()))
  values = 'VALUES ({values})'.format(values="'" + "','".join(str(v) for v in data.values()) + "'")
  conflict_values = ''
  for key in data.keys():
    conflict_values += key + "='" + str(data[key]) + "',"

  conflict = ' ON CONFLICT(id) DO UPDATE SET {values}'.format(values=conflict_values[:-1])
  cur.execute(columns + values + conflict)

  #
  # Commit all records.
  # And close cursor and connection.
  #
  conn.commit()
  cur.close()
  conn.close()
