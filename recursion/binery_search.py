def binary_search(arr, low, high, item):
    if low <= high:
        n = len(arr)
        mid = (low+high)//2
        if arr[mid] == item:
            return item, mid
        elif arr[mid] > item:
            return binary_search(arr, low, mid - 1, item)
        elif arr[mid] < item:
            return binary_search(arr, mid + 1, high, item)
    else:
        return -1


print(binary_search([4, 3, 15], 0, 2, 15))
