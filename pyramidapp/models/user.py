# vim: set fileencoding=utf-8 :
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

from sqlalchemy.orm import relationship

from . import (
    BASE,
    Dateable,
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


class User(BASE, Dateable):
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
    def by_login(cls, login):
        """
        Get a user with the login
        """
        # pylint: disable=E1101
        return DB_SESSION.query(User).filter(User.login == login).first()

    @classmethod
    def by_login_password(cls, login, password):
        """
        Get a user with the login and password
        """
        # pylint: disable=E1101
        query = DB_SESSION.query(User)
        filter1 = query.filter(User.login == login)
        return filter1.filter(User.password == password).first()

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
    """
    Class to access to the user groups
    """
    def __init__(self, obj, parent):
        """
        Constructor
        """
        self.obj = obj
        self.parent = parent

    @property
    def groupname(self):
        """
        Accessor to the groupName
        """
        return self.obj.name

    @groupname.setter
    def groupname(self, value):
        """
        Setter of the group name
        Doesn't do anything
        """
        pass

    @property
    def access(self):
        """
        Know if a group in access by a user
        """
        return self.obj in self.parent.groups

    @access.setter
    def access(self, value):
        """
        Set or unset a access group to the user
        """
        if value is True and self.obj not in self.parent.groups:
            self.parent.groups.append(self.obj)
        elif value is False and self.obj in self.parent.groups:
            self.parent.groups.remove(self.obj)


class UserGroupAccess(object):
    """
    Class to manage a user with group relation
    """
    def __init__(self, obj):
        """
        Constructor
        """
        self.obj = obj

    @property
    def login(self):
        """
        Getter for the login
        """
        return self.obj.login

    @login.setter
    def login(self, value):
        """
        Setter for the login
        """
        self.obj.login = value

    @property
    def email(self):
        """
        Getter for the email
        """
        return self.obj.email

    @email.setter
    def email(self, value):
        """
        Setter for the email
        """
        self.obj.email = value

    @property
    def firstname(self):
        """
        Getter for the firstname
        """
        return self.obj.firstname

    @firstname.setter
    def firstname(self, value):
        """
        Setter for the firstname
        """
        self.obj.firstname = value

    @property
    def lastname(self):
        """
        Getter for the lastname
        """
        return self.obj.lastname

    @lastname.setter
    def lastname(self, value):
        """
        Setter for the lastname
        """
        self.obj.lastname = value

    @property
    def password(self):
        """
        Getter for the password
        """
        pass

    @password.setter
    def password(self, value):
        """
        Setter for the password
        """
        self.obj.password = value

    @property
    def groups(self):
        """
        Getter for the groups
        """
        for group in Group.all():
            yield GroupAccess(group, self.obj)

    @groups.setter
    def groups(self, values):
        """
        Setter for the groups
        """
        pass
