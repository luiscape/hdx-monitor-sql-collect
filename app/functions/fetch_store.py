#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Function that fetches data from a given class
and handles the output doing either

  (a) storing a successful response in the database
  (b) creating an user-intended error message

This function was designed to be called by the
Redis Queue function. It is processed as a set
of background jobs.

'''
from app.utilities.item import item
from app.functions.store_data import storeData
from app.functions.fetch_class_data import fetchClassData
from app.functions.fetch_resource_data import fetchResourceData

def fetchAndStore(key=None, id=None):
  '''
  Collects data from a class and handles its output either
  by storing it in a database or by constructing an error
  message to be delivered to the user.

  '''
  if key == 'resources':
    data = fetchResourceData(dataset_id=id)
    for resource in data:
      storeData(resource, key)

  else:
    data = fetchClassData(key, id)
    if data:
      storeData(data, key)
