import unittest

from program import add_tem_to_list

class MyFunctionTest(unittest.TestCase):

    def test_my_function(self):
        self.assertEqual(add_tem_to_list(1, 2), 3)