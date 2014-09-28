# coding : utf-8
"""
This is a unit test for Right model
"""
import unittest

from pyramidapp.models.right import Right

from . import init_testing_db


class TestRight(unittest.TestCase):
    # pylint: disable=R0904
    #    Too many pyblic methods: we are a subclass of unittest.TestCase
    """
    Test of right
    """
    def setUp(self):
        self.db_session = init_testing_db()

    def tearDown(self):
        self.db_session.remove()

    def test_right_basic(self):
        """
        This test all access to the bdd for Right
         - Insert
         - Select
         - Update
         - Delete
        """
        # pylint: disable=E1101
        self.db_session.add(Right("read"))
        self.db_session.commit()

        acc1 = self.db_session.query(Right).filter_by(name="read").scalar()
        self.assertEquals(acc1.name, "read")

        self.db_session.add(Right("edit"))
        self.db_session.add(Right("delete"))
        self.db_session.commit()

        self.assertEquals(self.db_session.query(Right).count(), 3)

        acc1 = self.db_session.query(Right).filter_by(name="read").scalar()
        acc1.name = "READ"
        self.db_session.commit()

        acc1 = self.db_session.query(Right).filter_by(name="READ").scalar()
        self.assertEquals(acc1.name, "READ")

        self.db_session.delete(acc1)
        self.db_session.commit()

        self.assertEquals(self.db_session.query(Right).count(), 2)
        # pylint: enable=E1101
