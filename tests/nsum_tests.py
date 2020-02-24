import unittest

from algo.nsum import NSum

class TestProblem(unittest.TestCase):

    def setUp(self) -> None:
        self.arr1 = [14, 18, 4, 5, 7, 8, 10, 13, 24, 37, 19, 21, 1, 3, 40, 45, 71]

    def test_two_sum(self):
        self.assertTrue(NSum.two_sum_brute_force(self.arr1, 20))
        self.assertFalse(NSum.two_sum_brute_force(self.arr1, 1000))

    def test_three_sum(self):
        self.assertTrue(NSum.three_sum_brute_force(self.arr1, 20))
        self.assertFalse(NSum.three_sum_brute_force(self.arr1, 1000))


if __name__ == '__main__':
    unittest.main()
