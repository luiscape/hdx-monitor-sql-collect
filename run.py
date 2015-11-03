#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
HDX Monitor SQL Collect is an application that
collect data from a CKAN instance and organizes it
in 7 database tables. The tables were designed for
the use of `Metabase` for quick analysis
and exploration.

'''
from app.server import createServer

def main():
  '''
  Wrapper function for starting SQL collect.

  '''
  server = createServer('test', debug=True)
  server.run()


if __name__ == '__main__':
    main()
