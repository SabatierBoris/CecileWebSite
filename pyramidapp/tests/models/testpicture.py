# vim: set fileencoding=utf-8 :
"""
This is a unit test for Picture model
"""
import unittest

from pyramidapp.models.picture import Picture

from . import init_testing_db


class TestPicture(unittest.TestCase):
    """
    Test of picture
    """
    def setUp(self):
        self.db_session = init_testing_db()

    def tearDown(self):
        self.db_session.remove()

    def test_picture_basic(self):
        """
        This test all access to the bdd for Picture
         - Insert
         - Select
         - Update
         - Delete
        """
        # pylint: disable=E1101
        self.db_session.add(Picture(name="Muss"))
        self.db_session.commit()

        acc1 = self.db_session.query(Picture).filter_by(name="Muss").scalar()
        self.assertEquals(acc1.name, "Muss")

        self.db_session.add(Picture(name="Dessin"))
        self.db_session.add(Picture(name="Photos"))
        self.db_session.commit()

        self.assertEquals(self.db_session.query(Picture).count(), 3)

        acc1 = self.db_session.query(Picture).filter_by(name="Muss").scalar()
        acc1.name = "MUSS"
        self.db_session.commit()

        acc1 = self.db_session.query(Picture).filter_by(name="MUSS").scalar()
        self.assertEquals(acc1.name, "MUSS")

        self.db_session.delete(acc1)
        self.db_session.commit()

        self.assertEquals(self.db_session.query(Picture).count(), 2)
       # pylint: enable=E1101
