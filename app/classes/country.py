#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
CKAN Country class (formally known as "group").
This class fetches all relevant information about
a country / group from a specified CKAN instance.

'''
import ckanapi

from app.classes.ckan import CKAN

class Country:
  '''
  Complete CKAN country class.

  '''
  def __init__(self, id):
    self.id = id
    self.ckan = CKAN().init()

  def info(self):
    self.object = self.ckan.action.group_show(id=self.id)
    return self.object
