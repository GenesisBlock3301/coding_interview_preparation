def isValid(matrix):
    rows = [set() for _ in range(len(matrix))]
    cols = [set() for _ in range(len(matrix))]
    mx_n = max(matrix[0])
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            m = matrix[r][c]
            if m >= 1 and m <= mx_n:
                if (m in rows[r] or m in cols[c]):
                    return False
            if len(rows) != len(cols):
                return False
            rows[r].add(m)
            cols[c].add(m)

    return True


matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
# matrix = [[1, 1, 1], [1, 2, 3], [1, 2, 3]]
print(isValid(matrix))
