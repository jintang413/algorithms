class QuickFindUF:

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