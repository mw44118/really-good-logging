# vim: set expandtab ts=4 sw=4 filetype=python:

import logging
import sys
import traceback

def f():

    return g()

def g():

    return h()

def h():

    return i()

def i():

    1/0

def log_uncaught_exceptions(ex_cls, ex, tb):

    logging.critical(''.join(traceback.format_tb(tb)))
    logging.critical('{0}: {1}'.format(ex_cls, ex))

if __name__ == '__main__':

    logging.basicConfig(
        level=logging.DEBUG,
        filename='/tmp/kaboom2.log',
        filemode='w')

    sys.excepthook = log_uncaught_exceptions

    logging.debug('About to do f().')

    f()
