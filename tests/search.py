import unittest

from algo.search import binary_search


class TestSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.arr = [1, 3, 4, 5, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]

    def test_binary_search(self):
        lb_idx = 0
        ub_idx = len(self.arr) - 1

        self.assertEqual(-1, binary_search([], 1, 0, 1))
        self.assertEqual(-1, binary_search([], 1, 0, -1))
        self.assertEqual(-1, binary_search(self.arr, 100, lb_idx, ub_idx))
        self.assertEqual(lb_idx, binary_search(self.arr, 1, lb_idx, ub_idx))
        self.assertEqual(ub_idx, binary_search(self.arr, 71, lb_idx, ub_idx))
        self.assertEqual(8, binary_search(self.arr, 14, lb_idx, ub_idx))
        self.assertEqual(3, binary_search(self.arr, 5, lb_idx, ub_idx))
        self.assertEqual(14, binary_search(self.arr, 40, lb_idx, ub_idx))


if __name__ == '__main__':
    unittest.main()
