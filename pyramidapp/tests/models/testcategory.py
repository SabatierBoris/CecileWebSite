# vim: set fileencoding=utf-8 :
"""
This is a unit test for Category model
"""
import unittest

from pyramidapp.models.category import Category

from . import init_testing_db


class TestCategory(unittest.TestCase):
    """
    Test of category
    """
    def setUp(self):
        self.db_session = init_testing_db()

    def tearDown(self):
        self.db_session.remove()

    def test_category_basic(self):
        """
        This test all access to the bdd for Category
         - Insert
         - Select
         - Update
         - Delete
        """
        # pylint: disable=E1101
        self.db_session.add(Category(name="Muss"))
        self.db_session.commit()

        acc1 = self.db_session.query(Category).filter_by(name="Muss").scalar()
        self.assertEquals(acc1.name, "Muss")

        self.db_session.add(Category(name="Dessin"))
        self.db_session.add(Category(name="Photos"))
        self.db_session.commit()

        self.assertEquals(self.db_session.query(Category).count(), 3)

        acc1 = self.db_session.query(Category).filter_by(name="Muss").scalar()
        acc1.name = "MUSS"
        self.db_session.commit()

        acc1 = self.db_session.query(Category).filter_by(name="MUSS").scalar()
        self.assertEquals(acc1.name, "MUSS")

        self.db_session.delete(acc1)
        self.db_session.commit()

        self.assertEquals(self.db_session.query(Category).count(), 2)
       # pylint: enable=E1101

    def test_category_parent(self):
        # TODO
        pass
