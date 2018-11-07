import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)

    def test_sub(self):
        result = rpn.calculate("1 1 -")
        self.assertEqual(0, result)

    def test_mult(self):
        result = rpn.calculate("1 3 *")
        self.assertEqual(3, result)

    def test_floor_div(self):
        result = rpn.calculate("2 1 -")
        self.assertEqual(1, result)
