def split_land(n, m):
    if n < m:
        return n
    print(n, m)
    return split_land(n - m, m)


def recursive_sum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + recursive_sum(arr[1:])


# print(split_land(1680, 640))
# print(split_land(640, 240))
print(recursive_sum([2, 4, 6]))
