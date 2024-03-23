# 1020. Number of Enclaves
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.


# Example 1:


# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
# Example 2:


# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is either 0 or 1.


class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
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
                if nR >= 0 and nC >= 0 and nR < m and nC < n and (nR, nC) not in visited and board[nR][nC] == 1:
                    dfs(nR, nC)

        for i in range(m):
            if board[i][0] == 1:
                dfs(i, 0)
            if board[i][n-1] == 1:
                dfs(i, n-1)

        for i in range(n):
            if board[0][i] == 1:
                dfs(0, i)
            if board[m-1][i] == 1:
                dfs(m-1, i)
        count = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and board[i][j] == 1:
                    count += 1

        return count
