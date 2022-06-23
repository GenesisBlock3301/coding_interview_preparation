def fibonacci1(first, second, nth, arr):
    if nth == 0:
        return arr
    # if second not in arr:
    arr.append(second)
    nth -= 1
    return fibonacci1(second, first+second, nth, arr)


def fibonacci2(nth):
    if nth < 2:
        return nth
    return fibonacci2(nth-2)+fibonacci2(nth-1)

# arr = [0]
nth = 10
# print(fibonacci1(0, 1, nth, arr))
arr1 = []
ans = fibonacci2(nth)
print(ans)