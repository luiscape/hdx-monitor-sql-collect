#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Function to load data from CKAN object classes.

'''
from app.classes.user import User
from app.classes.country import Country
from app.classes.dataset import Dataset
from app.classes.revision import Revision
from app.classes.resource import Resource
from app.classes.gallery_item import GalleryItem

def fetchClassData(key=None, id=None):
  '''
  Loads data from specified CKAN object class.

  '''
  classes = {
      'user': User(id),
      'country': Country(id),
      'dataset': Dataset(id),
      'revision': Revision(id),
      'resource': Resource(id),
      'gallery_item': GalleryItem(id)
    }

  return { 'job': None, 'queue': None, 'data': classes.get(key).info() }
