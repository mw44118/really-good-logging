# vim: set expandtab ts=4 sw=4 filetype=python:

"""
Show how to use two loggers, each with their own handlers, so that
different log messages land in different files.
"""

import logging
import logging.handlers

def configure_logger_for_parsing_code():

    logger_for_parsing_code = logging.getLogger('parser')

    logger_for_parsing_code.setLevel(logging.DEBUG)

    # Only keep the most recent one-thousand bytes in this file.
    parsing_handler = logging.FileHandler('/var/log/rgl/parser.log')

    parsing_handler.setLevel(logging.DEBUG)

    f = logging.Formatter(
        '%(asctime)s '
        '%(levelname)-10s '
        '%(process)-6d '
        '%(filename)-24s '
        '%(lineno)-4d '
        '%(message)s '
    )

    parsing_handler.setFormatter(f)

    logger_for_parsing_code.addHandler(parsing_handler)


def configure_logger_for_game_state_code():

    logger_for_game_state = logging.getLogger('gamestate')
    logger_for_game_state.setLevel(logging.DEBUG)

    f = logging.Formatter(
        '%(asctime)s '
        '%(levelname)-10s '
        '%(process)-6d '
        '%(filename)-24s '
        '%(lineno)-4d '
        '%(message)s '
    )

    gamestate_handler = logging.FileHandler('/var/log/rgl/gamestate.log')
    gamestate_handler.setLevel(logging.DEBUG)
    gamestate_handler.setFormatter(f)
    logger_for_game_state.addHandler(gamestate_handler)

def configure_logger_for_bugfix_checker():

    logger_for_bugfix_checker = logging.getLogger('bugfix')
    logger_for_bugfix_checker.setLevel(logging.DEBUG)

    # Do not send my log messages up to the root logger.
    logger_for_bugfix_checker.propagate = False

    f = logging.Formatter(
        '%(asctime)s '
        '%(levelname)-10s '
        '%(process)-6d '
        '%(filename)-24s '
        '%(lineno)-4d '
        '%(message)s '
    )

    bugfix_handler = logging.handlers.RotatingFileHandler(
        '/tmp/bugfix.log',
        maxBytes=800, backupCount=1)

    bugfix_handler.setLevel(logging.DEBUG)
    bugfix_handler.setFormatter(f)
    logger_for_bugfix_checker.addHandler(bugfix_handler)

def configure_root_logger():

    logging.root.setLevel(logging.DEBUG)
    h = logging.StreamHandler()
    h.setLevel(logging.DEBUG)
    logging.root.addHandler(h)

    f = logging.Formatter(
        '%(asctime)s '
        '%(levelname)-10s '
        '%(process)-6d '
        '%(filename)-24s '
        '%(lineno)-4d '
        '%(message)s '
    )

    h.setFormatter(f)

if __name__ == '__main__':

    configure_logger_for_parsing_code()
    configure_logger_for_game_state_code()
    configure_logger_for_bugfix_checker()
    configure_root_logger()

    gamestate_logger = logging.getLogger('gamestate')
    parser_logger = logging.getLogger('parser')

    parser_logger.debug("player command: look")
    gamestate_logger.debug("Retrieving room description...")

    parser_logger.debug("player command: north")
    gamestate_logger.debug("Updating player location")

    parser_logger.debug("player command: west")
    gamestate_logger.debug("Updating player location")

    parser_logger.debug("player command: look")
    gamestate_logger.debug("Retrieving room description...")

    parser_logger.debug("player command: invntory")
    parser_logger.error("Invalid command: 'invntory'")

    parser_logger.debug("player command: inventory")
    gamestate_logger.debug("Retrieving player inventory...")

    bugfix_logger = logging.getLogger('bugfix')

    for i in range(100):
        bugfix_logger.debug('checking...')
