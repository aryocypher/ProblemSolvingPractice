# Description
# Accepted
# Accepted
# Editorial
# Editorial
# Solutions
# Solutions
# Submissions
# Submissions


# Code
# Testcase
# Testcase
# Test Result
# 931. Minimum Falling Path Sum
# Solved
# Medium
# Topics
# Companies
# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

# Example 1:


# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
# Example 2:


# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        
        cache={}
        def rec(i,j):
            if i>=m or j>=n or j<0:
                return sys.maxsize
            if i==m-1:
                return matrix[i][j]
            if (i,j) in cache:
                return cache[(i,j)]
            downl=rec(i+1,j-1)
            downr=rec(i+1,j+1)
            downb=rec(i+1,j)

            cache[(i,j)]=min(downl,downr,downb)+matrix[i][j]
            return cache[(i,j)]
        
        minVal=sys.maxsize
        for i in range(n):
            minVal=min(rec(0,i),minVal)
        
        return minVal