import unittest
import nginpro.utils as utils


class UtilsTest(unittest.TestCase):
    def test_server_block(self):
        # check if server block returns a string
        self.assertIs(type(utils.make_block('server', 'server_name localhost;')), str)


