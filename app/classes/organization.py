#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
CKAN Organization class. This class fetches all
relevant information about a country / group
from a specified CKAN instance.

'''
import ckanapi

from app.classes.ckan import CKAN

class Organization:
  '''
  Complete CKAN organization class.

  '''
  def __init__(self, id):
    self.id = id
    self.ckan = CKAN().init()

  def info(self):
    self.object = self.ckan.action.organization_show(id=self.id)
    return self.object
