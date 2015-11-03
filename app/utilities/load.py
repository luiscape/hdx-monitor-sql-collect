#!/usr/bin/python
# -*- coding: utf-8 -*-

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

  return file
