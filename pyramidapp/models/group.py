# coding : utf-8
"""
Group Model module
"""
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import func

from sqlalchemy.orm import relationship

from . import (
    BASE,
    DB_SESSION,
)
from .right import Right


class Group(BASE):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    Group Model
    """
    __tablename__ = 'group'
    uid = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    rights = relationship('Right', secondary='group_right', backref='groups')
    created_on = Column(DateTime,
                        default=func.now())
    updated_on = Column(DateTime,
                        default=func.now(),
                        onupdate=func.now())

    def __init__(self, name=""):
        super(Group, self).__init__()
        self.name = name

    @classmethod
    def all(cls):
        """
        Get all groups
        """
        # pylint: disable=E1101
        return DB_SESSION.query(Group).all()

    @classmethod
    def by_uid(cls, uid):
        """
        Get a group with the uid
        """
        # pylint: disable=E1101
        return DB_SESSION.query(Group).filter(Group.uid == uid).first()

    @classmethod
    def get_session(cls):
        """
        Get the sqlalchemy session
        """
        return DB_SESSION


ASSOCIATION_TABLE = Table('group_right', BASE.metadata,
                          Column('group_id', Integer, ForeignKey(Group.uid)),
                          Column('right_id', Integer, ForeignKey(Right.uid)))


class RightAccess(object):
    def __init__(self, obj, parent):
        self.obj = obj
        self.parent = parent

    @property
    def rightName(self):
        return self.obj.name

    @rightName.setter
    def rightName(self, value):
        pass

    @property
    def access(self):
        return self.obj in self.parent.rights

    @access.setter
    def access(self, value):
        if value is True and self.obj not in self.parent.rights:
            self.parent.rights.append(self.obj)
        elif value is False and self.obj in self.parent.rights:
            self.parent.rights.remove(self.obj)


class GroupRightAccess(object):
    def __init__(self, obj):
        self.obj = obj

    @property
    def name(self):
        return self.obj.name

    @name.setter
    def name(self, value):
        self.obj.name = value

    @property
    def rights(self):
        for right in Right.all():
            yield(RightAccess(right, self.obj))

    @rights.setter
    def rights(self, values):
        pass
