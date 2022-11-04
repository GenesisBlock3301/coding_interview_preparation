def merge_sort(arr):
    length = len(arr)
    if length == 1:
        return arr

    mid = length // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    merge_list = list()
    l1 = len(left)
    l2 = len(right)
    i = 0
    j = 0
    while i < l1 and j < l2:
        if left[i] < right[j]:
            merge_list.append(left[i])
            i += 1
        else:
            merge_list.append(right[j])
            j += 1

    if i < l1:
        merge_list.extend(left[i:])
    elif j < l2:
        merge_list.extend(right[j:])
    return merge_list

# log n* n -> O(n log n)
print(merge_sort([5, 4, 3, 3, 2, 1]))
