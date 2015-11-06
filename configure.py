#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Configuring the application.

'''
from app.utilities.item import item
from app.database import createTables

def main():
  '''
  Wrapper function for configuration scripts.

  '''
  createTables()

  print('%s Created database table successfully.\n' % item('success'))

if __name__ == '__main__':
  main()
