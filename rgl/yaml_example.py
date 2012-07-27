# vim: set expandtab ts=4 sw=4 filetype=python:

import logging
import logging.config
import textwrap

import yaml

def configure_logging():

    yaml_style_config = textwrap.dedent("""
    version: 1

    root:
        level: DEBUG
        handlers: [console]

    handlers:
        console:
            class: logging.StreamHandler
            level: DEBUG
            formatter: consolefmt

    formatters:
        consolefmt:
            format: '%(asctime)s %(levelname)-10s %(process)-6d %(filename)-24s %(lineno)-4d %(message)s'

    """)

    d = yaml.load(yaml_style_config)

    logging.config.dictConfig(d)

if __name__ == '__main__':

    configure_logging()

    logging.debug('This is a boring debug message.')
    logging.info('Here is an info message...')
    logging.warn('This is a warning message!')
    logging.error('Even worse, This is an error message!')
    logging.critical('OH NO THIS IS CRITICAL')

    logging.info('All done!')
