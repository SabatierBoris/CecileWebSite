# coding : utf-8
"""
This is a unit test for Access model
"""
import unittest

from pyramidapp.models.access import Access

from . import init_testing_db


class TestAccess(unittest.TestCase):
    # pylint: disable=R0904
    #    Too many pyblic methods: we are a subclass of unittest.TestCase
    """
    Test of access
    """
    def setUp(self):
        self.bd_session = init_testing_db()

    def tearDown(self):
        self.bd_session.remove()

    def test_access_basic(self):
        """
        This test all access to the bdd for Access
         - Insert
         - Select
         - Update
         - Delete
        """
        # pylint: disable=E1101
        self.bd_session.add(Access("read"))
        self.bd_session.commit()

        acc1 = self.bd_session.query(Access).filter_by(name="read").scalar()
        self.assertEquals(acc1.name, "read")

        self.bd_session.add(Access("edit"))
        self.bd_session.add(Access("delete"))
        self.bd_session.commit()

        self.assertEquals(self.bd_session.query(Access).count(), 3)

        acc1 = self.bd_session.query(Access).filter_by(name="read").scalar()
        acc1.name = "READ"
        self.bd_session.commit()

        acc1 = self.bd_session.query(Access).filter_by(name="READ").scalar()
        self.assertEquals(acc1.name, "READ")

        self.bd_session.delete(acc1)
        self.bd_session.commit()

        self.assertEquals(self.bd_session.query(Access).count(), 2)
        # pylint: enable=E1101
