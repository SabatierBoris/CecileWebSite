"""
This module test the right administration view
"""
import unittest

from pyramid import testing

from pyramidapp.scripts.initializebd import main
from pyramidapp.models import DB_SESSION
from pyramidapp.models.right import Right


class RightAdministrationTest(unittest.TestCase):
    # pylint: disable=R0904
    #    Too many pyblic methods: we are a subclass of unittest.TestCase
    """
    Test the right administration part
    """
    def setUp(self):
        main(['pyramidapp/config/test.ini'])
        self.db_session = DB_SESSION
        help(DB_SESSION)

#        self.config = testing.setUp()
#        self.config.include('pyramid_mako')
        from pyramid.paster import get_app
        app = get_app('pyramidapp/config/test.ini')
        from webtest import TestApp
        self.testapp = TestApp(app)
        self.request = testing.DummyRequest()

    def tearDown(self):
        pass
#        self.db_session.remove()
#        testing.tearDown()

    def test_list_right(self):
        """
        Test the view of listing the right
        """
        res = self.testapp.get('/admin/right', status=200)
        self.assertIn(b'Liste des droits', res.body)
        # ADD RIGHT MANAGEMENT ACCESS TEST

        self.db_session.add(Right("delete"))  # pylint: disable=E1101
        self.db_session.commit()  # pylint: disable=E1101
        res = self.testapp.get('/admin/right', status=200)
        self.assertIn(b'delete', res.body)

#    def test_create_right(self):
#        """
#        Test the view of creating a right
#        """
#        res = self.testapp.get('/admin/right/new', status=200)
#        self.assertIn(b'Ajout d&#39;un droit', res.body)
#        # ADD RIGHT MANAGEMENT ACCESS TEST
#
#    def test_edit_right(self):
#        """
#        Test the view of editing a right
#        """
#        res = self.testapp.get('/admin/right/1/edit', status=200)
#        self.assertIn(b'Modification du droit administration', res.body)
#        # ADD RIGHT MANAGEMENT ACCESS TEST
