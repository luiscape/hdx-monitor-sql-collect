#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
CKAN Resouce class. This class fetches all
relevant information about a resource from
a specified CKAN instance.

'''
import ckanapi

from app.classes.ckan import CKAN

class Resource:
  '''
  Complete CKAN resource class.

  '''
  def __init__(self, id):
    self.id = id
    self.hdx = CKAN().init()

  def info(self):
    self.object = self.hdx.action.resource_show(id=self.id)
    return self.object
