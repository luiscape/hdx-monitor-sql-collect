#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
CKAN Dataset class (formally known as "package").
This class fetches all relevant information about
a dataset from a specified CKAN instance.

'''
import ckanapi

from app.classes.ckan import CKAN

class Dataset:
  '''
  Complete CKAN dataset class.

  '''
  def __init__(self, id):
    self.id = id
    self.hdx = CKAN().init()

  def info(self):
    self.object = self.hdx.action.package_show(id=self.id)
    return self.object
