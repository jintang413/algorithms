from utils.util import is_within_range


class QuickFindUF:

    def __init__(self, n: int):
        self._n = n
        self._id = list(range(n))
        self._validate_range = lambda x: is_within_range(x, ub=n-1)

    def union(self, p: int, q: int):
        pid = self.find(p)
        qid = self.find(q)
        for i in range(self._n):
            self._id[i] = qid if self._id[i] == pid else self._id[i]

    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)

    def find(self, p: int) -> int:
        if not self._validate_range(p):
            raise ValueError(f'Input of value {p} is not between 0 and {self._n - 1}.')
        return self._id[p]

    def count(self) -> int:
        return len(set(self._id))


class QuickUnionUF:

    def __init__(self, n: int):
        self._id = range(0, n)
        self._count = n

    def union(self, p: int, q: int):
        raise NotImplemented

    def connected(self, p: int, q: int):
        raise NotImplemented

    def find(self, p: int) -> int:
        raise NotImplemented

    def count(self) -> int:
        return self._count


class WeightedQuickUnionUF:
    def __init__(self, n: int):
        self._id = range(0, n)
        self._sz = [1] * n
        self._count = n

    def _root(self, i: int) -> int:
        raise NotImplemented

    def union(self, p: int, q: int):
        raise NotImplemented

    def connected(self, p: int, q: int):
        raise NotImplemented

    def find(self, p: int) -> int:
        raise NotImplemented

    def count(self) -> int:
        return self._count


class QuickUnionPathCompressionUF:
    def __init__(self, n: int):
        self._id = range(0, n)
        self._sz = [1] * n
        self._count = n

    def _root(self, i: int) -> int:
        raise NotImplemented

    def union(self, p: int, q: int):
        raise NotImplemented

    def connected(self, p: int, q: int):
        raise NotImplemented

    def find(self, p: int) -> int:
        raise NotImplemented

    def count(self) -> int:
        return self._count


class WeightedQuickUnionPathCompressionUF:
    def __init__(self, n: int):
        self._id = range(0, n)
        self._sz = [1] * n
        self._count = n

    def _root(self, i: int) -> int:
        raise NotImplemented

    def union(self, p: int, q: int):
        raise NotImplemented

    def connected(self, p: int, q: int):
        raise NotImplemented

    def find(self, p: int) -> int:
        raise NotImplemented

    def count(self) -> int:
        return self._count
