# 329. Longest Increasing Path in a Matrix
# Solved
# Hard
# Topics
# Companies
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).


# Example 1:


# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:


# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
# Example 3:

# Input: matrix = [[1]]
# Output: 1


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 231 - 1
class Solution:
    def longestIncreasingPath2D(self, matrix: List[List[int]]) -> int:
        maxVal = 0

        dp = {}

        def dfs(i, j, val):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == '.' or matrix[i][j] <= val:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            l, r, b, t = 0, 0, 0, 0
            temp = matrix[i][j]
            matrix[i][j] = '.'
            t = dfs(i-1, j, temp)
            b = dfs(i+1, j, temp)
            l = dfs(i, j-1, temp)
            r = dfs(i, j+1, temp)
            matrix[i][j] = temp
            dp[(i, j)] = max(t, b, l, r)+1

            return dp[(i, j)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxVal = max(maxVal, dfs(i, j, -sys.maxsize))

        return maxVal

    def longestIncreasingPath3D(self, matrix: List[List[int]]) -> int:
        maxVal = 0

        dp = {}

        def dfs(i, j, val):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == '.':
                return 0
            if (i, j, val) in dp:
                return dp[(i, j, val)]

            l, r, b, t = 0, 0, 0, 0
            if matrix[i][j] > val:
                temp = matrix[i][j]
                matrix[i][j] = '.'
                t = dfs(i-1, j, temp)
                b = dfs(i+1, j, temp)
                l = dfs(i, j-1, temp)
                r = dfs(i, j+1, temp)
                matrix[i][j] = temp
                dp[(i, j, val)] = max(t, b, l, r)+1
            else:
                dp[(i, j, val)] = 0

            return dp[(i, j, val)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxVal = max(maxVal, dfs(i, j, -sys.maxsize))

        return maxVal
