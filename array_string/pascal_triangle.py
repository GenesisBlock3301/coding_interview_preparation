def getRow(A):
    arr = [[0] * (i + 1) for i in range(A + 1)]
    for i in range(len(arr)):
        arr[i][0] = 1
        arr[i][-1] = 1

    for row in range(2, len(arr)):
        i = 1
        for val in range(1, len(arr[row - 1])):
            arr[row][i] = arr[row - 1][val - 1] + arr[row - 1][val]
            i += 1
    return arr[A]


print(getRow(3))


