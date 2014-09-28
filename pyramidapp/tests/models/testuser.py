# coding : utf-8
"""
This is a unit test for User model
"""
import unittest

import hashlib  # pylint: disable=F0401

from pyramidapp.models.group import Group
from pyramidapp.models.user import User

from . import init_testing_db


class TestUser(unittest.TestCase):
    # pylint: disable=R0904
    #    Too many pyblic methods: we are a subclass of unittest.TestCase
    """
    Test of User
    """
    def setUp(self):
        self.session = init_testing_db()

    def tearDown(self):
        self.session.remove()

    def test_user_basic(self):
        """
        Test all access to the bdd for User
         - Insert
         - Select
         - Update
         - Delete
        """
        # pylint: disable=E1101
        user = User("login", "password")
        user.firstname = "firstname"
        user.lastname = "lastname"
        user.email = "email@gmail.com"

        self.session.add(user)
        self.session.commit()

        query = self.session.query(User)
        query.filter_by(login="login")
        query.filter_by(password="password")
        user = query.scalar()

        hash1 = hashlib.sha512("notThePassword".encode("utf-8")).hexdigest()
        hash2 = hashlib.sha512("password".encode("utf-8")).hexdigest()
        hash3 = hashlib.sha512("bouboup".encode("utf-8")).hexdigest()
        hash4 = hashlib.sha512("Bouboup".encode("utf-8")).hexdigest()

        self.assertNotEquals(user, None)
        self.assertEquals(user.login, "login")
        self.assertEquals(user.firstname, "firstname")
        self.assertEquals(user.lastname, "lastname")
        self.assertEquals(user.email, "email@gmail.com")
        self.assertNotEquals(user.password, "password")
        self.assertNotEquals(user.password, hash1)
        self.assertEquals(user.password, hash2)

        user.password = "Bouboup"
        self.session.commit()

        query = self.session.query(User)
        query.filter_by(login="login")
        query.filter_by(password="Bouboup")
        user = query.scalar()

        self.assertNotEquals(user.password, "Bouboup")
        self.assertNotEquals(user.password, hash1)
        self.assertNotEquals(user.password, hash3)
        self.assertEquals(user.password, hash4)

        self.session.delete(user)
        self.session.commit()

        self.assertEquals(self.session.query(User).count(), 0)
        # pylint: enable=E1101

    def test_user_group(self):
        """
        Test the association of access to a group
        """
        # pylint: disable=E1101
        user = User("login", "password")
        group1 = Group('Reader')
        group2 = Group('Writer')

        self.session.add(user)
        self.session.add(group1)
        self.session.add(group2)
        self.session.commit()

        user = self.session.query(User).all()[0]
        self.assertEquals(user.groups, [])

        user.groups.append(group1)
        self.session.commit()
        user = self.session.query(User).all()[0]
        self.assertEquals(user.groups, [group1])

        user.groups.append(group2)
        self.session.commit()
        user = self.session.query(User).all()[0]
        self.assertEquals(user.groups, [group1, group2])

        user.groups.remove(group2)
        self.session.commit()
        user = self.session.query(User).all()[0]
        self.assertEquals(user.groups, [group1])
        # pylint: enable=E1101
