#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
CKAN User class. This class fetches all
relevant information about an user from
a specified CKAN instance.

'''
import ckanapi

from app.classes.ckan import CKAN

class User:
  '''
  Complete CKAN user class.

  '''
  def __init__(self, id):
    self.id = id
    self.ckan = CKAN().init()

  def info(self):
    self.object = self.ckan.action.user_show(id=self.id)
    return self.object
