# vim: set fileencoding=utf-8 :
"""
Module of the model part
"""
from sqlalchemy.ext.declarative import declarative_base, AbstractConcreteBase

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    func,
)

DB_SESSION = scoped_session(sessionmaker())
BASE = declarative_base()


class ModelBase(object):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    Utility models class for adding uid and some methods
    """
    uid = Column(Integer, primary_key=True)

    @classmethod
    def all(cls):
        """
        Get all elements
        """
        # pylint: disable=E1101
        return DB_SESSION.query(cls).all()

    @classmethod
    def by_uid(cls, uid):
        """
        Get a element with the uid
        """
        # pylint: disable=E1101
        return DB_SESSION.query(cls).filter(cls.uid == uid).first()

    @classmethod
    def get_session(cls):
        """
        Get the sqlalchemy session
        """
        return DB_SESSION

    def delete(self):
        try:
            super().delete()
        except:
            pass


class Dateable(ModelBase):
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

    def delete(self):
        try:
            super().delete()
        except:
            pass
    

import pyramidapp.models.right
import pyramidapp.models.group
import pyramidapp.models.user
import pyramidapp.models.item
import pyramidapp.models.category
import pyramidapp.models.tag
import pyramidapp.models.picture
import pyramidapp.models.link
