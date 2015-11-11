#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Function to load resource information. This
function uses instances from datasets to create
an iterable array of resources ids. Then uses that
array to create instances of resources.

'''
import app.utilities.load as Load

from app.classes.dataset import Dataset
from app.classes.resource import Resource

config = Load.loadJSONFile('config/dev.json')

def _fields(config, key):
  '''
  Extract field names from the database
  property in the configuration file.

  '''
  result = None
  for table in config['database']:
    if table['name'] == key:
      result = [ i['field_name'] for i in table['columns'] ]

  return result

def fetchResourceData(dataset_id):
  '''
  Fetch resource information from datasets.

  '''
  #
  # Creates a dataset instance
  # and collects an array with the
  # resource ids.
  #
  d = Dataset(dataset_id)
  d.info()
  resources = d.resources()
  resource_data = []
  for resource in resources:
    data = { k: Resource(resource).info()[k] for k in _fields(config, 'resources') }
    resource_data.append(data)

  #
  # Selects only the fields
  # of interest from the dictionary.
  #
  return resource_data
