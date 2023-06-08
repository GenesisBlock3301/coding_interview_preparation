from typing import List


def insertion_sort(arr: List) -> List:
    length = len(arr)
    for i in range(1, length):
        item = arr[i]
        j = i - 1
        while j>=0 and arr[j] > item:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = item
    return arr

arr = [5,4,3,2]
print(insertion_sort(arr))