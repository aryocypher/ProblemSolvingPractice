# 62. Unique Paths
# Solved
# Medium
# Topics
# Companies
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.


# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

class Solution:
    def uniquePathsRecursive(self, m: int, n: int) -> int:
        cache = []

        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(-1)
            cache.append(temp)

        def uniquePathRec(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if (i == m-1) and (j == n-1):
                return 1
            if cache[i][j] != -1:
                return cache[i][j]

            right = uniquePathRec(i+1, j)
            down = uniquePathRec(i, j+1)
            cache[i][j] = right+down
            return cache[i][j]
        return uniquePathRec(0, 0)


class Solution:
    def uniquePathsIte(self, m: int, n: int) -> int:
        cache = []

        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(-1)
            cache.append(temp)
        cache[m-1][n-1] = 1

        for i in range(m-1):
            cache[i][n-1] = 1

        for i in range(n-1):
            cache[m-1][i] = 1

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                cache[i][j] = cache[i+1][j]+cache[i][j+1]

        return cache[0][0]
