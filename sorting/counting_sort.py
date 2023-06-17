
def counting_sort(arr1):
    max_val = max(arr1) + 1
    size = len(arr1)
    count = [0]*max_val
    # output = [0]*size
    output = list()

    # simple count all elements
    for i in range(0, size):
        count[arr1[i]] += 1

    # loop for count cumulative sum
    # for m in range(1, max_val):
    #     count[m] += count[m-1]
    #
    # k = size - 1
    # while k >= 0:
    #     output[count[arr1[k]] - 1] = arr1[k]
    #     count[arr1[k]] -= 1
    #     k -= 1

    for i, val in enumerate(count):
        if val > 0:
            output.extend([i]*val)

    return output


arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))
