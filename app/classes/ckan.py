#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
CKAN default class. Here we define the CKAN
class with default values declared in the
configuration files.

'''
import ckanapi
import app.utilities.load as Load

class CKAN:
  '''
  CKAN class with the defaulf configurations of
  the CKAN instance at hand defined in the
  configuration files.

  '''
  def __init__(self, instance='dev'):
    instances = {
      'dev': 'config/dev.json',
      'prod': 'config/prod.json'
    }
    config = Load.loadJSONFile(instances.get(instance))
    ckan = ckanapi.RemoteCKAN(
        user_agent='ckanapi/1.0',
        apikey=config['ckan']['api'],
        address=config['ckan']['url']
      )
    self.ckan = ckan

  def init(self):
    return self.ckan
