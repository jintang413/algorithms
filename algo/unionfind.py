class QuickFindUF:

    def __init__(self, n: int):
        self._id = list(range(n))
        self._count = n

    def _validate(self, p: int):
        n = self._count
        if (p < 0) or (p >= n):
            raise Exception('p is not between 0 and %d.' % (n-1))

    def union(self, p: int, q: int):
        self._validate(p)
        self._validate(q)
        pid = self._id[p]
        qid = self._id[q]
        n = self._count
        for i, cid in enumerate(self._id):
            if cid == pid:
                self._id[i] = qid

    def connected(self, p: int, q: int):
        self._validate(p)
        self._validate(q)
        return self._id[p] == self._id[q]

    def find(self, p: int) -> int:
        self._validate(p)
        return self._id[p]

    def count(self) -> int:
        return self._count


class QuickUnionUF:

    def __init__(self, n: int):
        self._id = list(range(n))
        self._count = n

    def _validate(self, p: int):
        n = self._count
        if (p < 0) or (p >= n):
            raise Exception('p is not between 0 and %d.' % (n-1))

    def _root(self, p: int) -> int:
        self._validate(p)
        while p != self._id[p]:
            p = self._id[p]
        return p

    def union(self, p: int, q: int):
        self._validate(p)
        self._validate(q)
        rootp = self._root(p)
        rootq = self._root(q)
        self._id[rootp] = self._id[rootq]

    def connected(self, p: int, q: int):
        self._validate(p)
        self._validate(q)
        return self._root(p) == self._root(q)

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