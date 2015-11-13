#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Configuring a PostgreSQL database.

'''
import os
import psycopg2

from app.utilities.item import item
from app.utilities.load import loadJSONFile

DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
HOST_DATABASE = os.environ.get('POSTGRES_PORT_5432_TCP_ADDR')

def createTables(instance='config/dev.json', verbose=True):
  '''
  Creates tables in a PostgreSQL instance.

  '''
  #
  # Loading database information
  # from config file.
  #
  database = loadJSONFile(instance)['database']

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

  #
  # Build each table.
  #
  for table in database:

    #
    # Construct SQL statement.
    #
    table_sql = ""
    for column in table['columns']:
      s = '%s %s, ' % (column['field_name'], column['type'])
      table_sql += s

    statement = 'CREATE TABLE IF NOT EXISTS "%s" (%sPRIMARY KEY (%s))' % (table['name'], table_sql, ", ".join(table['primary_key']))

    #
    # Make statements to the database.
    #
    try:
      cur.execute(statement)
      conn.commit()
      print("%s table `%s` created." % (item('bullet'), str(table['name'])))

    except Exception as e:
      print('%s Table `%s` could not be created.' % (item('error'), table['name']))
      if verbose:
        print(e)
      return False

  #
  # Close communication.
  #
  cur.close()
  conn.close()
