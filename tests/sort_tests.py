import unittest

from algo.sort import merge_sort


class TestSort(unittest.TestCase):

    def setUp(self) -> None:
        self.unsorted_arr = [14, 18, 4, 5, 7, 8, 10, 13, 24, 37, 19, 21, 1, 3, 40, 45, 71]
        self.sorted_arr = [1, 3, 4, 5, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]

    def test_merge_sort(self):
        merge_sort(self.unsorted_arr, 0, len(self.unsorted_arr) - 1)
        self.assertListEqual(self.sorted_arr, self.unsorted_arr)


if __name__ == '__main__':
    unittest.main()
