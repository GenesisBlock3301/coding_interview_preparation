
def counting_sort(arr):
    max_val = max(arr) + 1
    size = len(arr)
    count = [0]*max_val
    output = [0]*size

    for i in range(0, size):
        count[arr[i]] += 1

    for m in range(1, max_val):
        count[m] += count[m-1]

    k = size - 1
    while k >= 0:
        output[count[arr[k]]-1] = arr[k]
        count[arr[k]] -= 1
        k -= 1

    return output


arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))
