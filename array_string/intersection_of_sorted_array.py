def intersect(A, B):
    ans = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            ans.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return ans


A = [1, 2, 3, 3, 4, 5, 6]
B = [3,3, 5]

print(intersect(A, B))
