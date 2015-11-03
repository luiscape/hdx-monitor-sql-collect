#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Creates and configures CKAN application instance.

'''
import os
import ckanapi
import app.utilities.load as Load

config = Load.loadJSONFile('config/dev.json')

def createCKANInstance():
  '''
  Creates CKAN application instance.

  '''
  ckan = ckanapi.RemoteCKAN(
      apikey=os.environ.get('CKAN_KEY', 'foo'),
      address=os.environ.get('https://data.hdx.rwlabs.org', 'baz'),
      user_agent='hdx-monitor-sql-collect-{version}'.format(version=config['version'])
    )

  return ckan
