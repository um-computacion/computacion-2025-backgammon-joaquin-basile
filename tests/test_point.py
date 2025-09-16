import unittest
from core.point import Point
from core.exceptions import InvalidMove, NoCheckers

class TestPoint(unittest.TestCase):
    def test_get_color(self):
        point = Point('w', 5)
        self.assertEqual(point.get_color(), 'w')
        point = Point('b', 3)
        self.assertEqual(point.get_color(), 'b')

    def test_get_quantity(self):
        point = Point('w', 5)
        self.assertEqual(point.get_quantity(), 5)
        point = Point('b', 0)
        self.assertEqual(point.get_quantity(), 0)

    def test_add_checker(self):
        point = Point('w', 5)
        point.add_checker('w')
        self.assertEqual(point.get_quantity(), 6)

    def test_add_checker_and_steal(self):
        point = Point('w', 1)
        stole = point.add_checker('b')
        self.assertTrue(stole)
        self.assertEqual(point.get_color(), 'b')
        self.assertEqual(point.get_quantity(), 1)

    def test_add_checker_different_color(self):
        point = Point('w', 5)
        with self.assertRaises(InvalidMove):
            point.add_checker('b')
        self.assertEqual(point.get_quantity(), 5)
        self.assertEqual(point.get_color(), 'w')

    def test_del_checker(self):
        point = Point('w', 5)
        point.del_checker()
        self.assertEqual(point.get_quantity(), 4)
        self.assertEqual(point.get_color(), 'w')

    def test_del_checker_empty(self):
        point = Point('w', 0)
        with self.assertRaises(NoCheckers):
            point.del_checker()
        self.assertEqual(point.get_quantity(), 0)
        self.assertEqual(point.get_color(), 'w')
