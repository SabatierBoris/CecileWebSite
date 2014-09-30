# coding : utf-8
"""
This module is used for initialized the bdd
"""

import sys
import argparse
import string
import random

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from ..models import (
    DB_SESSION,
    BASE,
)

from ..models.right import Right
from ..models.group import Group
from ..models.user import User


def generate_password(size=6, chars=string.ascii_letters+string.digits):
    """
    Create a random password of @size with @chars values
    """
    return ''.join(random.choice(chars) for _ in range(size))


def init_admin(session):
    """
    Create the admin if doesn't exist
    """
    password = None
    query = session.query(Right).filter_by(name='administration')
    right = query.scalar()
    if right is None:
        right = Right('administration')
        session.add(right)

    query = session.query(Group).filter_by(name='admins')
    group = query.scalar()
    if group is None:
        group = Group('admins')
        session.add(group)
    group.rights.append(right)

    query = session.query(User).filter_by(login="admin")
    admin = query.scalar()
    if admin is None:
        password = generate_password(size=10)
        admin = User("admin", password)
        session.add(admin)
    admin.groups.append(group)
    session.commit()
    if password:
        print("Admin password : %s" % password)


def main(argv=None):
    """
    Main function. Initialized the bdd
    """
    parser = argparse.ArgumentParser(description='Initialize the DataBase')
    parser.add_argument('config', help='Link to the config file')
    if argv is None:
        argv = sys.argv
        argv.pop(0)

    args = parser.parse_args(argv)

    config_uri = args.config
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DB_SESSION.configure(bind=engine)
    BASE.metadata.create_all(engine)
    init_admin(DB_SESSION)
