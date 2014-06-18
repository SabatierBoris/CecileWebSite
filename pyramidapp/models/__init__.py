# coding : utf-8
"""
Module of the model part
"""
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

DB_SESSION = scoped_session(sessionmaker())
BASE = declarative_base()
