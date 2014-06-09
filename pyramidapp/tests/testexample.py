"""
This is a example of a unittest module
"""
import unittest


class TestExample(unittest.TestCase):
    # pylint: disable-msg=R0904
    #    Too many pyblic methods: we are a subclass of unittest.TestCase
    """
    Test of test
    """
    def test_one(self):
        """
        This is a example of a unittest
        """
        self.assertFalse(True)
