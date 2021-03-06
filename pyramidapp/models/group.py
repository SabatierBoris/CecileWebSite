# vim: set fileencoding=utf-8 :
"""
Group Model module
"""

from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import relationship

from . import (
    Dateable,
    BASE,
)
from .right import Right


class Group(Dateable, BASE):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    Group Model
    """
    __tablename__ = 'group'
    name = Column(String,
                  unique=True,
                  nullable=False,
                  info={'trim': True})
    rights = relationship('Right', secondary='group_right', backref='groups')

    def __init__(self, name=""):
        super().__init__()
        self.name = name


ASSOCIATION_TABLE = Table('group_right', BASE.metadata,
                          Column('group_id', Integer, ForeignKey(Group.uid)),
                          Column('right_id', Integer, ForeignKey(Right.uid)))


class RightAccess(object):
    """
    Class to access to the group rights
    """
    def __init__(self, obj, parent):
        """
        Constructor
        """
        self.obj = obj
        self.parent = parent

    @property
    def rightname(self):
        """
        Accessor to the rightname
        """
        return self.obj.name

    @rightname.setter
    def rightname(self, value):
        """
        Setter of the right name
        Doesn't do anything
        """
        pass

    @property
    def access(self):
        """
        Know if a right in access by a group
        """
        return self.obj in self.parent.rights

    @access.setter
    def access(self, value):
        """
        Set or unset a access right to the group
        """
        if value is True and self.obj not in self.parent.rights:
            self.parent.rights.append(self.obj)
        elif value is False and self.obj in self.parent.rights:
            self.parent.rights.remove(self.obj)


class GroupRightAccess(object):
    """
    Class to manage a group with right relation
    """
    def __init__(self, obj):
        """
        Constructor
        """
        self.obj = obj

    @property
    def name(self):
        """
        Getter for the group name
        """
        return self.obj.name

    @name.setter
    def name(self, value):
        """
        Setter for the group name
        """
        self.obj.name = value

    @property
    def rights(self):
        """
        Getter for the rights
        """
        for right in Right.all():
            yield RightAccess(right, self.obj)

    @rights.setter
    def rights(self, values):
        """
        Setter for the rights
        Doesn't do anything
        """
        pass
