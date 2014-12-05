# vim: set fileencoding=utf-8 :
"""
This is a example of a unittest module
"""
import unittest


class TestExample(unittest.TestCase):
    """
    Test of test
    """
    def test_one(self):
        """
        This is a example of a unittest
        """
        self.assertFalse(False)

    def test_two(self):
        """
        This is a example of a unittest
        """
        self.assertTrue(True)
