# vim: set expandtab ts=4 sw=4 filetype=python:

"""
This script shows how to:

*   write everything of DEBUG or greater to stderr and /tmp/rgl.log;

*   write everything with level INFO or greater to /var/log/rgl/rgl.log;

*   email critical log messages.

*   Also, every log message has:

    *   date and time
    *   log level
    *   process ID
    *   line number of the log statement
    *   file name containing the log statement

WHERE ARE YOUR PRINT STATEMENTS NOW?
"""

import logging
import logging.handlers

def configure_logging():

    # Set the logger to DEBUG.
    logging.root.setLevel(logging.DEBUG)

    # Now write a custom formatter, so that we get all those different
    # things.
    f = logging.Formatter(
        '%(asctime)s '
        '%(levelname)-10s '
        '%(process)-6d '
        '%(filename)-24s '
        '%(lineno)-4d '
        '%(message)s '
    )

    # Set up a stream handler for DEBUG stuff (and greater).
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(f)
    logging.root.addHandler(sh)

    # Set up a file handler for DEBUG stuff and greater to go to /tmp.
    fh = logging.FileHandler('/tmp/rgl.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(f)
    logging.root.addHandler(fh)

    # Set up another file handler for INFO stuff and greater to go to
    # /var/log/rgl/rgl.log.
    fh2 = logging.FileHandler('/var/log/rgl/rgl.log')
    fh2.setLevel(logging.INFO)
    fh2.setFormatter(f)
    logging.root.addHandler(fh2)

    # Now do the email stuff.  Nothing really fancy here, just a
    # different handler and a different level.
    mh = logging.handlers.SMTPHandler(
        'localhost', # mail server
        'rgl@sprout.tplus1.com', # from address
        ['matt@tplus1.com'], # to address
        'CRITICAL ERROR LOG MESSAGE' # email subject
    )

    mh.setLevel(logging.CRITICAL)
    mh.setFormatter(f)
    logging.root.addHandler(mh)

if __name__ == '__main__':

    configure_logging()

    logging.debug('This is a boring debug message.')
    logging.info('Here is an info message...')
    logging.warn('This is a warning message!')
    logging.error('Even worse, This is an error message!')
    logging.critical('OH NO THIS IS CRITICAL')

    logging.info('All done!')
