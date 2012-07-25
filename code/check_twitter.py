# vim: set expandtab ts=4 sw=4 filetype=python:

"""
Does a search on twitter for the parameter passed in.
"""

import argparse
import httplib
import json
import logging
import urllib


def set_up_arguments():

    ap = argparse.ArgumentParser()

    ap.add_argument('search_term')

    return ap.parse_args()


if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG)

    args = set_up_arguments()

    logging.debug('search term is {0}.'.format(args.search_term))

    h = httplib.HTTPConnection('search.twitter.com')
    h.request('GET', '/search.json?q={0}'.format(urllib.quote(args.search_term)))

    r = h.getresponse()

    logging.info('status is {0}.'.format(r.status))

    j = r.read()

    parsed_json_data = json.loads(j)

    logging.debug(parsed_json_data.keys())
    logging.debug(parsed_json_data['results'][0])
