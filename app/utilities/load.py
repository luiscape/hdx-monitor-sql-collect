#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Helper function that loads contents from a
JSON file into a Python dictionary. This
script was designed to load configuration files
adding an API key if that hasn't been defined in
the appropriate configuration file property.

'''
import os
import json

def loadJSONFile(path=None):
  '''
  Loads JSON file and returns dictionary.

  Arguments:
    - path: full path to JSON file.

  Returns: dict

  '''

  with open(path) as json_file:
    file = json.load(json_file)

  if file["ckan"]["api"] is None:
    file["ckan"]["api"] = os.environ.get('CKAN_KEY')

  return file
