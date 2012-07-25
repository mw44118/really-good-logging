# vim: set expandtab ts=4 sw=4 filetype=python:

"""
Show the logging.basicConfig filename parameter.
"""

import argparse
import logging
import sys

if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG, filename='/tmp/out.log')

    logging.info('All done!')
