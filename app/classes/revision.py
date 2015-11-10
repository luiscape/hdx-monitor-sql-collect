#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
CKAN Revision class. This class fetches all
relevant information about a revision from
a specified CKAN instance.

This class will add the `action_type` key
to the revision object by searching for
the strings defined in the `self.categories`
object in the `message` string.

'''
import ckanapi

from app.classes.ckan import CKAN

class Revision:
  '''
  Complete CKAN revision class.

  '''
  def __init__(self, id):
    self.id = id
    self.ckan = CKAN().init()
    self.categories = ['Update', 'Create', 'Delete']

  def info(self):
    self.object = self.ckan.action.revision_show(id=self.id)
    for category in self.categories:
      message = self.object.get('message')
      if type(message) == type(''):
        result = message.find(category)
      else:
        result = -1

      if result > -1:
        self.object['action_type'] = category
      else:
        self.object['action_type'] = 'unknown'

    return self.object
