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
    self.hdx = CKAN().init()

  def info(self):
    self.object = self.hdx.action.related_show(id=self.id)
    return self.object
