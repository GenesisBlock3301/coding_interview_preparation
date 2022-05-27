def isValid(board):
    row = [set() for _ in range(9)]
    col = [set() for _ in range(9)]
    box = [set() for _ in range(9)]

    for r in range(len(board)):
        for c in range(len(board)):
            b = board[r][c]
            box_number = (r//3)*3+c//3
            if b != ".":
                if (b in row[r]) or (b in col[c]) or (b in box[box_number]):
                    return False
                row[r].add(b)
                col[c].add(b)
                box[box_number].add(b)

    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(isValid(board))
