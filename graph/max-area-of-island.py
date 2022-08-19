# https://leetcode.com/problems/max-area-of-island/


def numIslands(grid):
    row = len(grid)
    col = len(grid[0])
    max_island = []
    for i in range(row):
        for k in range(col):
            inner_island = []
            if grid[i][k] == 1:
                dfs(grid, i, k, inner_island)
                max_island.append(inner_island)
    return max([len(x) for x in max_island]) if len(max_island) > 0 else 0


def dfs(grid, i, j, max_island):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
        return
    grid[i][j] = "#"
    max_island.append(grid[i][j])
    dfs(grid, i + 1, j, max_island)
    dfs(grid, i - 1, j, max_island)
    dfs(grid, i, j + 1, max_island)
    dfs(grid, i, j - 1, max_island)


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
# [[0,0,0,0,0,0,0,0]]
#     [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]
print(numIslands(grid))
