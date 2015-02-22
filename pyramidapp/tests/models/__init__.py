# vim: set fileencoding=utf-8 :
"""
This module test the models part of the project
"""
from sqlalchemy import create_engine

from pyramidapp.models import (
    DB_SESSION,
    BASE
)

# pylint: disable=W0611
from pyramidapp.models.right import Right
from pyramidapp.models.group import Group
from pyramidapp.models.user import User
from pyramidapp.models.tag import Tag
from pyramidapp.models.item import Item
from pyramidapp.models.category import Category
from pyramidapp.models.picture import Picture
# pylint: enable=W0611


def init_testing_db():
    """
    Initialise the DB for testing
    """
    engine = create_engine('sqlite:///:memory:', echo=True)
    BASE.metadata.create_all(engine)
    DB_SESSION.configure(bind=engine)
    return DB_SESSION
