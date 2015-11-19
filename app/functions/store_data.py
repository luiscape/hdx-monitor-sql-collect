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

DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
HOST_DATABASE = os.environ.get('POSTGRES_PORT_5432_TCP_ADDR')

def storeData(data, table):
  '''
  Store records in a PostgreSQL database.

  '''
  #
  # TODO: add environment variables
  # to these default values.
  #
  conn = psycopg2.connect(
      host=HOST_DATABASE,
      dbname=DB_NAME,
      user=DB_USER,
      password=DB_PASSWORD
    )
  cur = conn.cursor()
  conn.set_client_encoding('UTF8')

  #
  # Check no NULL values are passed.
  #
  def _clean_null(data):
    '''
    Cleans nulls or empty stings from dictionaries.

    '''
    pops = []
    for key in data.keys():
      if data.get(key) is None or len(str(data.get(key))) == 0:
        pops.append(key)

    for key in pops:
      data.pop(key)

    return data

  def _conflict_values(data, keys):
    '''
    Create conflict values statement.

    '''
    conflict_values = ''
    for key in keys:
      conflict_values += key + "='" + str(data[key]).replace("'", "`") + "',"

    s = ' ON CONFLICT(id) DO UPDATE SET {values}'.format(values=conflict_values[:-1])
    return s

  #
  # Using `upsert` statement newly available
  # on PostgreSQL 9.5. We are using a beta version
  # of the database.
  #
  data = _clean_null(data)
  keys = data.keys()
  values = ','.join("'" + str(v).replace("'", "`") + "'" for v in data.values())
  statement = {
    'columns': 'INSERT INTO {table} ({columns}) '.format(table=table, columns=",".join(keys)),
    'values': 'VALUES (%s)' % values,
    'conflict': _conflict_values(data, keys)
  }
  print(type(values))
  # print(statement['values'])
  cur.execute(statement['columns'] + statement['values'] + statement['conflict'])

  #
  # Commit all records.
  # And close cursor and connection.
  #
  conn.commit()
  cur.close()
  conn.close()
