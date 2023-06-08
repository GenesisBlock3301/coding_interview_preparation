def quick_sort(arr):
    if len(arr) == 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


array = [5, 4, 2, 1, 4]
print(quick_sort(array))
