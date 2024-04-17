# 695. Max Area of Island
# Solved
# Medium
# Topics
# Companies
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res=0
        visited=set()
        def dfs(i,j):
            if (i,j) in visited or i>=len(grid) or j>=len(grid[0]) or i<0 or j<0:
                return 0

            visited.add((i,j))
            if grid[i][j]==1:
                return 1+dfs(i,j+1)+dfs(i,j-1)+dfs(i-1,j)+dfs(i+1,j)
            return 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1 and (r,c) not in visited:
                    res=max(res,dfs(r,c))
        return res