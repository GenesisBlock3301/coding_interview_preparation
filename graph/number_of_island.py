# https://leetcode.com/problems/number-of-islands/

def numIslands(grid):
    row = len(grid)
    col = len(grid[0])
    count = 0
    for i in range(row):
        for k in range(col):
            if grid[i][k] == "1":
                dfs(grid, i, k)
                count+=1
    return count


def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid)\
            or j >= len(grid[0]) or grid[i][j] != "1":
        return
    grid[i][j] = "#"
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(grid))
