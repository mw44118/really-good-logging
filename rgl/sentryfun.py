import argparse
import logging

from raven.handlers.logging import SentryHandler
from raven.conf import setup_logging

log = logging.getLogger('rgl')

def process_arguments():

    ap = argparse.ArgumentParser()

    ap.add_argument('sentryDSN',
        help='Looks like https://sdfdfasdff...')

    return ap.parse_args()


def configure_logging(sentryDSN):

    """
    This is slightly different than the typical set up.  The handler
    acts like a regular handler, but sentry provides a function
    "setup_logging" that adds the handler to the root logger, and then
    also sets up a bunch of other loggers and handlers that don't
    propagate to the root.

    The point there is so that logging messages from sentry itself don't
    get sent to your sentry account.

    Also, I don't think it would be wise to set my own custom formatter
    for the sentry handler.
    """

    sentry_handler = SentryHandler('http://public:secret@example.com/1')
    setup_logging(sentry_handler)


def f():
    x = 'inside f'
    return g()

def g():
    x = 'inside g'
    return h()

def h():
    x = 'inside h'
    return i()

def i():

    x = 'inside i'
    1/0


if __name__ == '__main__':

    args = process_arguments()
    configure_logging(args.sentryDSN)

    log.debug('This is a boring debug message.')
    log.info('Here is an info message...')
    log.warn('This is a warning message!')
    log.error('Even worse, This is an error message!')
    log.critical('OH NO THIS IS CRITICAL')

    logging.info('All done!')

    try:
        f()

    except Exception as ex:
        log.exception(ex)

    log.info('All done!')
