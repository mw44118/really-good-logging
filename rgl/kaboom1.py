# vim: set expandtab ts=4 sw=4 filetype=python:

import logging

def f():
    return g()

def g():
    return h()

def h():
    return i()

def i():
    1/0

if __name__ == '__main__':

    logging.basicConfig(
        level=logging.DEBUG,
        filename='/tmp/kaboom1.log',
        filemode='w')

    logging.debug('About to do f().')

    f()
