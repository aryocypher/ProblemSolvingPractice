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
 

# Constraints:

# 1 <= m, n <= 100

#Most optimal Solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prev=[1]*n   
        for i in range(1,m):
            curr=[1]*n
            for j in range(1,n):
                curr[j]=prev[j]+curr[j-1]
            prev=curr

        return prev[n-1]
    

#Ite solution
    def uniquePathsIt(self, m: int, n: int) -> int:
        if m==1 and n==1:
            return 1
        cache=[[0 for i in range(n)] for j in range(m)]

        for i in range(1,m):
            cache[i][0]=1

        for j in range(1,n):
            cache[0][j]=1

        print(cache)
        
        for i in range(1,m):
            for j in range(1,n):
                cache[i][j]=cache[i-1][j]+cache[i][j-1]

        return cache[m-1][n-1]
    

#Rec solution
    def uniquePathsRec(self, m: int, n: int) -> int:
        
        cache={}
        def rec(i,j):
            if i==m or j==n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if (i,j) in cache:
                return cache[(i,j)]
            down=rec(i+1,j)
            right=rec(i,j+1)

            cache[(i,j)]= down+right
            return cache[(i,j)]
        
        return rec(0,0)