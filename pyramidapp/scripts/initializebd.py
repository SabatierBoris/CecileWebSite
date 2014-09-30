# coding : utf-8
"""
This module is used for initialized the bdd
"""

import sys
import argparse

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from ..models import (
    DB_SESSION,
    BASE,
)

from ..models.right import Right  # pylint: disable=W0611
from ..models.group import Group    # pylint: disable=W0611
from ..models.user import User      # pylint: disable=W0611


def main(argv=None):
    """
    Main function. Initialized the bdd
    """
    parser = argparse.ArgumentParser(description='Initialize the DataBase')
    parser.add_argument('config', help='Link to the config file')
    if argv is None:
        argv = sys.argv
        argv.pop(0)

    args = parser.parse_args(argv)

    config_uri = args.config
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DB_SESSION.configure(bind=engine)
    BASE.metadata.create_all(engine)
