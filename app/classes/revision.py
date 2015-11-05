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
    self.hdx = CKAN().init()
    self.categories = ['Update', 'Create', 'Delete']

  def info(self):
    self.object = self.hdx.action.revision_show(id=self.id)
    for category in self.categories:
      result = self.object['message'].find(category)
      if result > -1:
        self.object['action_type'] = category

    return self.object
