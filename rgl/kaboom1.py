# vim: set expandtab ts=4 sw=4 filetype=python:

import logging
import sys
import traceback

log = logging.getLogger('kaboom')

def f():

    return g()

def g():

    return h()

def h():

    return i()

def i():

    1/0

if __name__ == '__main__':

    log.debug('About to do f().')

    f()
