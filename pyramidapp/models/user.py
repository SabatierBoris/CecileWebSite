# coding : utf-8
"""
User Model module
"""
import hashlib  # pylint: disable=F0401

from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import types
from sqlalchemy import DateTime
from sqlalchemy import func

from sqlalchemy.orm import relationship

from . import (
    BASE,
    DB_SESSION,
)
from .group import Group


class MyPassword(types.TypeDecorator):
    # pylint: disable=R0904
    #    Too many pyblic methods: we are a subclass of TypeDecorator
    """
    Password type for sh512 management
    """
    impl = types.String

    def process_bind_param(self, value, dialect):
        return hashlib.sha512(value.encode("utf-8")).hexdigest()

    def process_result_value(self, value, dialect):
        return value

    def python_type(self):
        return str

    def process_literal_param(self, value, dialect):
        pass


class User(BASE):
    # pylint: disable=R0903
    #    Too fee pyblic methods: we are juste a model
    """
    User model
    """
    __tablename__ = 'user'
    uid = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    password = Column('password', MyPassword)
    groups = relationship('Group', secondary='user_group', backref='users')
    created_on = Column(DateTime,
                        default=func.now())
    updated_on = Column(DateTime,
                        default=func.now(),
                        onupdate=func.now())

    def __init__(self, login="", password=""):
        super(User, self).__init__()
        self.login = login
        self.password = password

    @classmethod
    def all(cls):
        """
        Get all users
        """
        # pylint: disable=E1101
        return DB_SESSION.query(User).all()

    @classmethod
    def by_uid(cls, uid):
        """
        Get a user with the uid
        """
        # pylint: disable=E1101
        return DB_SESSION.query(User).filter(User.uid == uid).first()

    @classmethod
    def get_session(cls):
        """
        Get the sqlalchemy session
        """
        return DB_SESSION

ASSOCIATION_TABLE = Table('user_group', BASE.metadata,
                          Column('user_id', Integer, ForeignKey(User.uid)),
                          Column('group_id', Integer, ForeignKey(Group.uid)))


class GroupAccess(object):
    def __init__(self, obj, parent):
        self.obj = obj
        self.parent = parent

    @property
    def groupName(self):
        return self.obj.name

    @groupName.setter
    def groupName(self, value):
        pass

    @property
    def access(self):
        return self.obj in self.parent.groups

    @access.setter
    def access(self, value):
        if value is True and self.obj not in self.parent.groups:
            self.parent.groups.append(self.obj)
        elif value is False and self.obj in self.parent.groups:
            self.parent.groups.remove(self.obj)


class UserGroupAccess(object):
    def __init__(self, obj):
        self.obj = obj

    @property
    def login(self):
        return self.obj.login

    @login.setter
    def login(self, value):
        self.obj.login = value

    @property
    def email(self):
        return self.obj.email

    @email.setter
    def email(self, value):
        self.obj.email = value

    @property
    def firstname(self):
        return self.obj.firstname

    @firstname.setter
    def firstname(self, value):
        self.obj.firstname = value

    @property
    def lastname(self):
        return self.obj.lastname

    @lastname.setter
    def lastname(self, value):
        self.obj.lastname = value

    @property
    def password(self):
        return ""

    @password.setter
    def password(self, value):
        self.obj.password = value

    @property
    def groups(self):
        for group in Group.all():
            yield(GroupAccess(group, self.obj))

    @groups.setter
    def groups(self, values):
        pass
