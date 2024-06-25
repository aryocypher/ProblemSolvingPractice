# 1091. Shortest Path in Binary Matrix
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.


# Example 1:


# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:


# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1

class Solution:
    def isValid(self,i,j,m,n):
        if i<0 or j<0 or i>=m or j>=m:
            return False
        return True

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        n,m=len(grid),len(grid[0])
        distGrid=[[sys.maxsize for _ in range(m)]for _ in range(n)]
        pq=[]
        heapq.heappush(pq,(1,0,0))
        distGrid[0][0]=1
        r=[-1,-1,-1,0,0,1,1,1]
        c=[-1,0,1,-1,1,-1,0,1]
        while pq:
            curr=heapq.heappop(pq)
            dist=curr[0]
            curR=curr[1]
            curC=curr[2]
            for i in range(len(r)):
                for j in range(len(c)):
                    nR=curR+r[i]
                    nC=curC+c[j]
                    if self.isValid(nR,nC,m,n) and grid[nR][nC]==0 and distGrid[nR][nC]>dist+1:
                        distGrid[nR][nC]=dist+1
                        heapq.heappush(pq,(dist+1,nR,nC))

        return distGrid[n-1][m-1] if distGrid[n-1][m-1]!=sys.maxsize else -1
        
