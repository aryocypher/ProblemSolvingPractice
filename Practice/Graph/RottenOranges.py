# 994. Rotting Oranges
# Solved
# Medium
# Topics
# Companies
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
class Solution:
    def isValid(self, i, j, m, n, visited):
        if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited:
            return False
        return True

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        maxSec = 0
        visited = set()
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited.add((i, j))
        while q:

            curr = q.popleft()
            r = curr[0]
            c = curr[1]
            s = curr[2]
            grid[r][c] = 2
            maxSec = max(s, maxSec)

            if self.isValid(r-1, c, m, n, visited) and grid[r-1][c] == 1:
                q.append((r-1, c, s+1))
                visited.add((r-1, c))
            if self.isValid(r, c-1, m, n, visited) and grid[r][c-1] == 1:
                q.append((r, c-1, s+1))
                visited.add((r, c-1))
            if self.isValid(r+1, c, m, n, visited) and grid[r+1][c] == 1:
                q.append((r+1, c, s+1))
                visited.add((r+1, c))
            if self.isValid(r, c+1, m, n, visited) and grid[r][c+1] == 1:
                q.append((r, c+1, s+1))
                visited.add((r, c+1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return maxSec
