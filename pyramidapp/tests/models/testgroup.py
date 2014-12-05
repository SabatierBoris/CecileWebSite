# vim: set fileencoding=utf-8 :
"""
This is a unit test for Group model
"""
import unittest

from pyramidapp.models.right import Right
from pyramidapp.models.group import Group

from . import init_testing_db


class TestGroup(unittest.TestCase):
    """
    Test of group
    """
    def setUp(self):
        self.session = init_testing_db()

    def tearDown(self):
        self.session.remove()

    def test_group_basic(self):
        """
        Test all access to the bdd for Group
         - Insert
         - Select
         - Update
         - Delete
        """
        # pylint: disable=E1101
        self.session.add(Group("reader"))
        self.session.commit()
        gp1 = self.session.query(Group).filter_by(name="reader").scalar()
        self.assertEquals(gp1.name, "reader")

        self.session.add(Group("Editor"))
        self.session.commit()

        self.assertEquals(self.session.query(Group).count(), 2)

        gp1 = self.session.query(Group).filter_by(name="reader").scalar()
        gp1.name = "Reader"
        self.session.commit()

        gp1 = self.session.query(Group).filter_by(name="Reader").scalar()
        self.assertEquals(gp1.name, "Reader")

        self.session.delete(gp1)
        self.session.commit()

        self.assertEquals(self.session.query(Group).count(), 1)
        # pylint: enable=E1101

    def test_group_right(self):
        """
        Test the association of right to a group
        """
        acc1 = Right('read')
        acc2 = Right('write')
        gp1 = Group('Reader')

        # pylint: disable=E1101
        self.session.add(acc1)
        self.session.add(acc2)
        self.session.add(gp1)
        self.session.commit()

        gp1 = self.session.query(Group).filter_by(name="Reader").scalar()
        self.assertEquals(gp1.rights, [])

        gp1.rights.append(acc1)
        self.session.commit()
        gp1 = self.session.query(Group).filter_by(name="Reader").scalar()
        self.assertEquals(gp1.rights, [acc1])

        gp1.rights.append(acc2)
        self.session.commit()
        gp1 = self.session.query(Group).filter_by(name="Reader").scalar()
        self.assertEquals(gp1.rights, [acc1, acc2])

        gp1.rights.remove(acc2)
        self.session.commit()
        gp1 = self.session.query(Group).filter_by(name="Reader").scalar()
        self.assertEquals(gp1.rights, [acc1])
        # pylint: enable=E1101
