import unittest

from algo.unionfind import QuickFindUF


class TestUnionFind(unittest.TestCase):

    def setUp(self) -> None:
        self.N = 10
        self.unions = [
            (4, 3),
            (3, 8),
            (6, 5),
            (9, 4),
            (2, 1),
            (8, 9),
            (5, 0),
            (7, 2),
            (6, 1),
            (1, 0),
            (6, 7)
        ]

    def test_quickfind_uf(self):
        uf = QuickFindUF(self.N)
        for p, q in self.unions:
            uf.union(p, q)

        expected_groups = 2
        group1 = {3, 4, 8, 9}
        group2 = {0, 1, 2, 5, 6, 7}

        self.assertEqual(expected_groups, uf.count())
        self.assertTrue(uf.connected(4, 8))
        self.assertTrue(uf.connected(3, 9))
        self.assertFalse(uf.connected(3, 0))
        self.assertTrue(uf.connected(1, 7))
        self.assertTrue(uf.connected(5, 2))
        self.assertFalse(uf.connected(8, 5))
        self.assertRaises(ValueError,uf.find, -1)
        self.assertRaises(ValueError, uf.find, 10)


if __name__ == '__main__':
    unittest.main()
