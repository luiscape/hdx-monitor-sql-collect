#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Function to load data from CKAN object classes.

'''
import app.utilities.load as Load

from app.classes.user import User
from app.classes.country import Country
from app.classes.dataset import Dataset
from app.classes.revision import Revision
from app.classes.resource import Resource
from app.classes.gallery_item import GalleryItem

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

def fetchClassData(key=None, id=None):
  '''
  Loads data from specified CKAN object class.

  '''
  classes = {
      'users': User(id),
      'countries': Country(id),
      'datasets': Dataset(id),
      'revisions': Revision(id),
      'resources': Resource(id),
      'gallery_items': GalleryItem(id)
    }

  #
  # Selects only the fields
  # of interest from the dictionary.
  #
  result = { k: classes[key].info()[k] for k in _fields(config, key) }
  return result
