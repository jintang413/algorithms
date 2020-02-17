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

    def _root(self, i: int) -> int:
        self._validate(i)
        while i != self._id[i]:
            i = self._id[i]
        return i

    def union(self, p: int, q: int):
        """Quick Union"""
        self._validate(p)
        self._validate(q)
        rootp = self._root(p)
        rootq = self._root(q)
        if rootp == rootq:
            return
        self._id[rootp] = rootq

    def connected(self, p: int, q: int):
        self._validate(p)
        self._validate(q)
        return self._root(p) == self._root(q)

    def count(self) -> int:
        return self._count


class WeightedQuickUnionUF:
    def __init__(self, n: int):
        self._id = list(range(n))
        self._sz = [1] * n
        self._count = n

    def _validate(self, p: int):
        n = self._count
        if (p < 0) or (p >= n):
            raise Exception('p is not between 0 and %d.' % (n-1))

    def _root(self, i: int) -> int:
        self._validate(i)
        while i != self._id[i]:
            i = self._id[i]
        return i

    def union(self, p: int, q: int):
        """Weighted Quick Union"""
        self._validate(p)
        self._validate(q)
        rootp = self._root(p)
        rootq = self._root(q)

        if rootp == rootq:
            return

        if self._sz[rootp] < self._sz[rootq]:
            self._id[rootp] = rootq
            self._sz[rootq] += self._sz[rootp]
        else:
            self._id[rootq] = rootp
            self._sz[rootp] += self._sz[rootq]

    def connected(self, p: int, q: int):
        self._validate(p)
        self._validate(q)
        return self._root(p) == self._root(q)

    def count(self) -> int:
        return self._count


class QuickUnionPathCompressionUF:
    def __init__(self, n: int):
        self._id = list(range(n))
        self._sz = [1] * n
        self._count = n

    def _validate(self, p: int):
        n = self._count
        if (p < 0) or (p >= n):
            raise Exception('p is not between 0 and %d.' % (n-1))

    def _root(self, i: int) -> int:
        """Path Compression"""
        self._validate(i)
        while i != self._id[i]:
            self._id[i] = self._id[self._id[i]]
            i = self._id[i]
        return i

    def union(self, p: int, q: int):
        """Quick Union"""
        self._validate(p)
        self._validate(q)
        rootp = self._root(p)
        rootq = self._root(q)

        if rootp == rootq:
            return
        self._id[rootp] = rootq

    def connected(self, p: int, q: int):
        self._validate(p)
        self._validate(q)
        return self._root(p) == self._root(q)

    def count(self) -> int:
        return self._count


class WeightedQuickUnionPathCompressionUF:
    def __init__(self, n: int):
        self._id = list(range(n))
        self._sz = [1] * n
        self._count = n

    def _validate(self, p: int):
        n = self._count
        if (p < 0) or (p >= n):
            raise Exception('p is not between 0 and %d.' % (n-1))

    def _root(self, i: int) -> int:
        """Path Compression"""
        self._validate(i)
        while i != self._id[i]:
            self._id[i] = self._id[self._id[i]]
            i = self._id[i]
        return i

    def union(self, p: int, q: int):
        """Weighted Quick Union"""
        self._validate(p)
        self._validate(q)
        rootp = self._root(p)
        rootq = self._root(q)

        if rootp == rootq:
            return

        if self._sz[rootp] < self._sz[rootq]:
            self._id[rootp] = rootq
            self._sz[rootq] += self._sz[rootp]
        else:
            self._id[rootq] = rootp
            self._sz[rootp] += self._sz[rootq]

    def connected(self, p: int, q: int):
        self._validate(p)
        self._validate(q)
        return self._root(p) == self._root(q)

    def count(self) -> int:
        return self._count

