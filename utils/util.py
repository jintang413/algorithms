def is_within_range(v, ub: int, lb: int = 0) -> bool:
    return v >= lb and v <= ub


def recurse_by_index(arr, i, compress=False):
    if i == arr[i]:
        return i
    else:
        if compress:
            arr[i] = arr[arr[i]]
        return recurse_by_index(arr, arr[i])
