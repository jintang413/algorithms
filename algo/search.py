def binary_search(arr, value, lb, ub):
    m = lb + (ub - lb) // 2

    if len(arr) == 0 or lb > ub:
        return -1
    elif arr[m] == value:
        return m
    else:
        if value < arr[m]:
            return binary_search(arr, value, lb, m - 1)
        else:
            return binary_search(arr, value, m + 1, ub)
