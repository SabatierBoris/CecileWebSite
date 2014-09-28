# coding : utf-8
"""
Right Model module
"""
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
)

from . import (
    BASE,
    DB_SESSION,
)


class Right(BASE):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    Right Model
    """
    __tablename__ = 'right'
    uid = Column(Integer, primary_key=True)
    name = Column(String,
                  unique=True,
                  nullable=False,
                  info={'trim': True})
    created_on = Column(DateTime,
                        default=func.now())
    updated_on = Column(DateTime,
                        default=func.now(),
                        onupdate=func.now())

    def __init__(self, name=""):
        super(Right, self).__init__()
        self.name = name

    @classmethod
    def all(cls):
        """
        Get all rights
        """
        # pylint: disable=E1101
        return DB_SESSION.query(Right).all()

    @classmethod
    def by_uid(cls, uid):
        """
        Get a right with the uid
        """
        # pylint: disable=E1101
        return DB_SESSION.query(Right).filter(Right.uid == uid).first()

    @classmethod
    def get_session(cls):
        """
        Get the sqlalchemy session
        """
        return DB_SESSION
