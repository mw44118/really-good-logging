# vim: set expandtab ts=4 sw=4 filetype=python:

import inspect
import logging
import sys
import traceback

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

    logging.basicConfig(level=logging.DEBUG)

    try:
        f()

    except Exception as ex:
        t, v, tb = sys.exc_info()
        stack_point = tb

        while stack_point:
            logging
            logging.debug(stack_point.tb_frame.f_locals)
            stack_point = stack_point.tb_next

    logging.debug("all done")
