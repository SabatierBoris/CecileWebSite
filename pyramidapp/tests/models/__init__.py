# vim: set fileencoding=utf-8 :
"""
This module test the models part of the project
"""
from sqlalchemy import create_engine

from pyramidapp.models import (
    DB_SESSION,
    BASE
)

from pyramidapp.models.right import Right    # pylint: disable=W0611
from pyramidapp.models.group import Group    # pylint: disable=W0611
from pyramidapp.models.user import User      # pylint: disable=W0611


def init_testing_db():
    """
    Initialise the DB for testing
    """
    engine = create_engine('sqlite:///:memory:', echo=True)
    BASE.metadata.create_all(engine)
    DB_SESSION.configure(bind=engine)
    return DB_SESSION
