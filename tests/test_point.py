import unittest
from core.point import Point
from core.exceptions import InvalidMove, NoCheckers
from core.const import black, white

class TestPoint(unittest.TestCase):
    def test_get_color(self):
        point = Point(white, 5)
        self.assertEqual(point.get_color(), white)
        point = Point(black, 3)
        self.assertEqual(point.get_color(), black)

    def test_add_checker(self):
        point = Point(white, 5)
        point.add_checker(white)
        self.assertEqual(point.get_quantity(), 6)

    def test_add_checker_and_steal(self):
        point = Point(white, 1)
        stole = point.add_checker(black)
        self.assertTrue(stole)
        self.assertEqual(point.get_color(), black)
        self.assertEqual(point.get_quantity(), 1)

    def test_add_checker_different_color(self):
        point = Point(white, 5)
        with self.assertRaises(InvalidMove):
            point.add_checker(black)
        self.assertEqual(point.get_quantity(), 5)
        self.assertEqual(point.get_color(), white)

    def test_del_checker(self):
        point = Point(white, 5)
        point.del_checker()
        self.assertEqual(point.get_quantity(), 4)
        self.assertEqual(point.get_color(), white)

    def test_del_checker_empty(self):
        point = Point(white, 0)
        with self.assertRaises(NoCheckers):
            point.del_checker()
        self.assertEqual(point.get_quantity(), 0)
        self.assertEqual(point.get_color(), white)
