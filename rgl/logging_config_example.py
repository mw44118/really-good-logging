# vim: set expandtab ts=4 sw=4 filetype=python:

import logging
import logging.config

import pkg_resources

def configure_logging():

    path_to_config_file = pkg_resources.resource_filename(
        'rgl.logging_configs',
        'simple_example.cfg')

    logging.config.fileConfig(path_to_config_file)

if __name__ == '__main__':

    configure_logging()

    logging.debug('This is a boring debug message.')
    logging.info('Here is an info message...')
    logging.warn('This is a warning message!')
    logging.error('Even worse, This is an error message!')
    logging.critical('OH NO THIS IS CRITICAL')

    logging.info('All done!')
