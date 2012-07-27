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

def set_up_logging():

    f = logging.Formatter(
        '%(asctime)-22s '
        '%(name)-12s '
        '%(levelname)-8s '
        '%(module)s '
        '%(filename)s '
        '%(lineno)s '
        '%(message)s'
    )

    h1 = logging.FileHandler('/tmp/kaboom.log', mode='w')
    h1.setFormatter(f)
    logging.root.addHandler(h1)

    h2 = logging.StreamHandler()
    h2.setFormatter(f)
    logging.root.addHandler(h2)

    logging.root.setLevel(logging.DEBUG)
    log.debug('Finished setting up logging')

def log_uncaught_exceptions(ex_cls, ex, tb):

    logging.critical(''.join(traceback.format_tb(tb)))
    logging.critical('{0}: {1}'.format(ex_cls, ex))

if __name__ == '__main__':

    set_up_logging()

    # sys.excepthook = log_uncaught_exceptions

    log.debug('About to do f().')

    f()
