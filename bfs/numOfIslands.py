# https://leetcode.cn/problems/number-of-islands/
from typing import List
import collections

''' Draft

Island

[['1', '1', '1', '1', '0'],
 ['1', '1', '0', '1', '0'],
 ['1', '1', '0', '0', '0'],
 ['0', '0', '0', '0', '0']]

[['1', '1', '0', '0', '0'],
 ['1', '1', '0', '0', '0'],
 ['0', '0', '1', '0', '0'],
 ['0', '0', '0', '1', '1']]

'''


class Solution_BFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr, nc = len(grid), len(grid[0])
        num_islands = 0

        if nr == 0:
            return 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]: # noqa
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1": # noqa
                                neighbors.append((x, y))
                                grid[x][y] = "0"

        return num_islands


class Solution_DFS:

    pass
