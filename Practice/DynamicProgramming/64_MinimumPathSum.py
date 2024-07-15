# 64. Minimum Path Sum
# Solved
# Medium
# Topics
# Companies
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

 

# Example 1:


# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200
class Solution:
    #optimized iterative
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        prev=[grid[0][0]]
        for i in range(1,n):
            prev.append(prev[-1]+grid[0][i])

        for i in range(1,m):
            curr=[0]*n
            curr[0]=prev[0]+grid[i][0]
            for j in range(1,n):
                val=min(prev[j],curr[j-1])+grid[i][j]
                curr[j]=val
            prev=curr
            
        return prev[n-1]
            

        
    def minPathSumRec(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        
        cache={}
        def rec(i,j):
            if i>=m or j>=n:
                return sys.maxsize
            if i==m-1 and j==n-1:
                return grid[i][j]
            if (i,j) in cache:
                return cache[(i,j)]
            down=rec(i+1,j)
            right=rec(i,j+1)

            cache[(i,j)]=min(down,right)+grid[i][j]
            return cache[(i,j)]
        

        return rec(0,0)