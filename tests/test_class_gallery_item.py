#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for testing the GalleryItem class.

'''
import os
import unittest

from app.classes.gallery_item import GalleryItem

class TestClassGalleryItem:
  '''
  Performs tests on the GalleryItem class.

  '''
  def __init__(self):
    self.keys = [
        'description','view_count','url',
        'title','image_url','type','id',
        'owner_id'
      ]

  def test_dataset_keys(self):
    '''
    classes.gallery_item:  Test that the GalleryItem class returns the right keys.

    '''
    result = GalleryItem('753ccf05-872f-4c8d-9cc2-8e562f6fc1d5').info()

    for key in self.keys:
      assert key in result.keys()

