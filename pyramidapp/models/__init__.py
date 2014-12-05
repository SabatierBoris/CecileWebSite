# vim: set fileencoding=utf-8 :
"""
Module of the model part
"""
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from sqlalchemy import (
    Column,
    DateTime,
    func,
)

DB_SESSION = scoped_session(sessionmaker())
BASE = declarative_base()


class Dateable(object):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    Utility class for adding created and updated date on table
    """
    created_on = Column(DateTime,
                        default=func.now())
    updated_on = Column(DateTime,
                        default=func.now(),
                        onupdate=func.now())
