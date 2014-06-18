# coding : utf-8
"""
User Model module
"""
import hashlib

from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import types

from sqlalchemy.orm import relationship

from . import BASE
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

    def __init__(self, login, password):
        super(User, self).__init__()
        self.login = login
        self.password = password

ASSOCIATION_TABLE = Table('user_group', BASE.metadata,
                          Column('user_id', Integer, ForeignKey(User.uid)),
                          Column('group_id', Integer, ForeignKey(Group.uid)))
