# t
# 130. Surrounded Regions
# Solved
# Medium
# Topics
# Companies
# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.


# Example 1:


# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
# Example 2:

# Input: board = [["X"]]
# Output: [["X"]]


# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        visited = set()
        rM = [-1, 1, 0, 0]
        rC = [0, 0, -1, 1]

        def dfs(r, c):
            print(r, c)
            visited.add((r, c))
            for i in range(4):
                nR = r+rM[i]
                nC = c+rC[i]
                if nR >= 0 and nC >= 0 and nR < m and nC < n and (nR, nC) not in visited and board[nR][nC] == 'O':
                    dfs(nR, nC)

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n-1] == 'O':
                dfs(i, n-1)

        for i in range(n):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[m-1][i] == 'O':
                dfs(m-1, i)

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    board[i][j] = 'X'
