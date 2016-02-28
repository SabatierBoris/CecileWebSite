# vim: set fileencoding=utf-8 :
"""
This module is used for initialized the thumbnail
"""

import sys
import argparse
import string
import random
import logging
import os

from sqlalchemy import engine_from_config

from pyramid.threadlocal import get_current_registry

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from ..models import (
    DB_SESSION,
    BASE,
)

from ..models.item import Item
# pylint: enable=W0611


LOGGER = logging.getLogger(__name__)

def main(argv=None):
    """
    Main function. Initialized the bdd
    """
    parser = argparse.ArgumentParser(description='Initialize thumbnails')
    parser.add_argument('config', help='Link to the config file')
    if argv is None:
        argv = sys.argv
        argv.pop(0)

    args = parser.parse_args(argv)

    config_uri = args.config
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    get_current_registry().settings = settings
    if 'DB_URL' in os.environ:
        engine = engine_from_config(settings, 'sqlalchemy.', url=os.environ['DB_URL'])
    else:
        engine = engine_from_config(settings, 'sqlalchemy.')
    DB_SESSION.configure(bind=engine)

    for item in Item.all():
        item.do_not_generate=True
        if item.thumbnail and os.path.isfile(item.thumbnail):
            os.remove(item.thumbnail)
        if item.thumbnailover and os.path.isfile(item.thumbnailover):
            os.remove(item.thumbnailover)

    for item in Item.all():
        item.thumbnail
        item.thumbnailover
