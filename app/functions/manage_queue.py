#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Function to manage the Redis Queue. In summary
this function either

  (a) starts a new queue if no jobs are pending
  (b) fetches statistics from a running queue
  (c) cancels a queue and starts again

This function was designed to be called directly
by the routes so that the final user knows what
is the current status of the running queues.

'''
