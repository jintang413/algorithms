class NSum:

    @staticmethod
    def two_sum_brute_force(arr, sum_to):
        n = len(arr) - 1
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if arr[i] + arr[j] == sum_to:
                    print(arr[i], arr[j])

    @staticmethod
    def two_sum_sort(arr, sum_to):
        raise NotImplemented

    @staticmethod
    def two_sum_hash(arr, sum_to):
        raise NotImplemented

    @staticmethod
    def three_sum_brute_force(arr, sum_to):
        n = len(arr) - 1
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if arr[i] + arr[j] + arr[k] == sum_to:
                        print(arr[i], arr[j], arr[k])

        return False

    @staticmethod
    def three_sum_sort(arr, sum_to):
        raise NotImplemented

    @staticmethod
    def three_sum_hash(arr, sum_to):
        raise NotImplemented