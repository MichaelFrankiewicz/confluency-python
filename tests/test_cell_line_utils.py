import unittest
from src.utils.cell_line_utils import find_doubling_time
import os

class TestDoublingTime(unittest.TestCase):

    def test_known_cell_line(self):
        path = os.path.join('data', 'cellosaurus.txt')
        self.assertEqual(find_doubling_time('HeLa', path), 24.0)

    def test_days_conversion(self):
        path = os.path.join('data', 'cellosaurus.txt')
        self.assertEqual(find_doubling_time('Panc-1', path), 60.0)

    def test_unknown_cell_line(self):
        path = os.path.join('data', 'cellosaurus.txt')
        self.assertIsNone(find_doubling_time('UnknownLine', path))

if __name__ == '__main__':
    unittest.main()
