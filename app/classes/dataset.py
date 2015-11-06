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
    self.ckan = CKAN().init()

  def info(self):
    self.object = self.ckan.action.package_show(id=self.id)
    self.object['tracking_summary_total'] = self.object['tracking_summary']['total']
    self.object['tracking_summary_recent'] = self.object['tracking_summary']['recent']
    self.object.pop('tracking_summary')
    return self.object
