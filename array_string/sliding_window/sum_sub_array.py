def min_sum_subarray(arr, K):
    min_sum = float('inf')
    window_sum = 0
    min_sum = 0
    for right in range(len(arr)):
        window_sum += arr[right]

        if right >= K - 1:
            min_sum = min(min_sum, window_sum)
            window_sum -= arr[right - (K - 1)]

    return min_sum


def max_sum_subarray(arr, K):
    max_sum = float("-inf")
    window_sum = 0

    for i in range(len(arr)):
        window_sum += arr[i]

        if i >= K - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[i - (K - 1)]
    return max_sum


print(min_sum_subarray([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(max_sum_subarray([1, 3, -1, -3, 5, 3, 6, 7], 3))
x = 2
y = (x := x * 2) + x
print(y)