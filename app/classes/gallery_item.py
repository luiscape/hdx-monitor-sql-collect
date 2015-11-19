#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
CKAN Gallery Item class (formally known as "related").
This class fetches all relevant information about
a gallery items / related items from a specified
CKAN instance.

'''
import ckanapi

from app.classes.ckan import CKAN

class GalleryItem:
  '''
  Complete CKAN gallery item / related item class.

  '''
  def __init__(self, id):
    self.id = id
    self.ckan = CKAN().init()

  def info(self):
    self.object = self.ckan.action.related_show(id=self.id)
    self.object['view_count'] = self.object['__extras']['view_count']
    self.object.pop('__extras')

    #
    # Filling missing values.
    #
    missing = ['image_url']
    for m in missing:
      if self.object.get(m) is None:
        self.object[m] = None

    return self.object
