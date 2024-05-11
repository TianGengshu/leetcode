# https://leetcode.cn/problems/surrounded-regions/
from collections import deque
from typing import List


class Solution:
    def solve(self,  board: List[List[str]]) -> None:
        """
        Do not return anything,  modify board in-place instead.
        """
        if not board:
            return

        n,  m = len(board),  len(board[0])
        queue = deque()

        # get all the O that's at the side
        # put into queue and marked as "A"
        for i in range(n):
            if board[i][0] == 'O':
                queue.append((i, 0))
                board[i][0] = 'A'
            if board[i][m-1] == 'O':
                queue.append((i, m-1))
                board[i][m-1] = 'A'
        for i in range(m):
            if board[0][i] == 'O':
                queue.append((0, i))
                board[0][i] = 'A'
            if board[n-1][i] == 'O':
                queue.append((n-1, i))
                board[n-1][i] = 'A'

        while queue:
            x, y = queue.popleft()
            for mx, my in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= mx < n and 0 <= my < m and board[mx][my] == 'O':
                    queue.append((mx, my))
                    board[mx][my] = 'A'

        # finally replace all O->X, A->O
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'
