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

  try:
    for record in data:

      #
      # Check no NULL values are passed.
      #
      for key in record.keys():
        if record.get(key) is None:
          record.pop(key)

      #
      # TODO: Check that the upsert statement
      # is supported by PostgreSQL 9.5. This
      #
      c = 'INSERT INTO {table} ({columns}) '.format(table=table, columns=",".join(record.keys()))
      v = 'VALUES ({values}) ON CONFLICT UPDATE'.format(values="'" + "','".join(str(v) for v in record.values()) + "'")
      # v = 'VALUES ({values})'.format(values="'" + "','".join(str(v) for v in record.values()) + "'")
      cur.execute(c + v)

    #
    # Commit all records.
    # And close cursor and connection.
    #
    conn.commit()
    cur.close()
    conn.close()

  except Exception as e:
    if e.pgcode == '23505':
      print('%s Record already exists. Skipping.' % item('warn'))
      return

    else:
      print("%s Failed to store record in database." % item('error'))
      print('PosgreSQL error code: %s' % e.pgcode)
      return False
