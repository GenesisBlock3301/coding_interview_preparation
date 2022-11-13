def count_number_element(arr):
    if len(arr) == 0:
        return 0
    return 1 + count_number_element(arr[1:])


def find_maximum_element(arr, index):
    if len(arr) - 2 < index:
        return arr[index]

    mx = find_maximum_element(arr, index+1)
    if arr[index] > mx:
        return arr[index]
    else:
        return mx


print(find_maximum_element([2, 3, 5], 0))
