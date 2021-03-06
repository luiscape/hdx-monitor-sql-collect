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
    self.ckan = CKAN().init()

  def info(self):
    self.object = self.ckan.action.resource_show(id=self.id)
    self.object['tracking_summary_total'] = self.object['tracking_summary']['total']
    self.object['tracking_summary_recent'] = self.object['tracking_summary']['recent']
    self.object.pop('tracking_summary')

    #
    # Filling missing values.
    # For some reason `None` is
    # not accepted by the database.
    #
    missing = ['resource_uploader', 'datastore_active']
    for m in missing:
      if self.object.get(m) is None:
        self.object[m] = None

    return self.object
