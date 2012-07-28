# vim: set expandtab ts=4 sw=4 filetype=python:

import logging
import logging.handlers

def f():

    return g()

def g():

    return h()

def h():

    return i()

def i():

    1/0

if __name__ == '__main__':

    logging.root.setLevel(logging.DEBUG)
    sh = logging.handlers.SysLogHandler('/dev/log')
    sh.setLevel(logging.DEBUG)

    logging.root.addHandler(sh)

    fmt = logging.Formatter(
        '%(asctime)s '
        '%(levelname)-10s '
        '%(process)-6d '
        '%(filename)-24s '
        '%(lineno)-4d '
        '%(message)s '
    )

    sh.setFormatter(fmt)

    h2 = logging.StreamHandler()
    h2.setLevel(logging.DEBUG)
    h2.setFormatter(fmt)
    logging.root.addHandler(h2)

    logging.debug('This is a boring debug message.')
    logging.info('Here is an info message...')
    logging.warn('This is a warning message!')
    logging.error('Even worse, This is an error message!')
    logging.critical('OH NO THIS IS CRITICAL')

    try:
        f()

    except Exception as ex:
        logging.exception(ex)
