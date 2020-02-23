def merge_sort(arr, lb, ub):
    if lb < ub:
        m = lb + (ub - lb) // 2
        merge_sort(arr, lb, m)
        merge_sort(arr, m + 1, ub)
        _merge(arr, lb, m, ub)


def _merge(arr, lb, m, ub):
    lb1 = lb
    lb2 = m + 1

    # already sorted
    if arr[m] <= arr[lb2]:
        return
    # loop until we hit the end of each subset
    while lb1 <= m and lb2 <= ub:

        if arr[lb1] <= arr[lb2]:
            lb1 += 1
        else:
            tmp_val = arr[lb2]
            tmp_idx = lb2
            # tmp_end_idx = tmp_start_idx
            # we could do an optimization here
            # shift = 1
            # while arr[lb_1] > arr[tmp_end_idx]
            #   tmp_end_idx+=1
            #   shift+=1

            while tmp_idx != lb1:
                arr[tmp_idx] = arr[tmp_idx - 1]
                tmp_idx -= 1

            arr[lb1] = tmp_val

            lb1 += 1
            lb2 += 1
            m += 1
