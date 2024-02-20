# 74. Search a 2D Matrix
# Solved
# Medium
# Topics
# Companies
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.


# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        top, bot = 0, R-1
        mid = 0
        while top <= bot:
            mid = (top+bot)//2
            if target > matrix[mid][-1]:
                top = mid+1
            elif target < matrix[mid][0]:
                bot = mid-1
            else:
                break

        if not top <= bot:
            return False

        l, r = 0, C

        while l <= r:
            m = (l+r)//2
            if target == matrix[mid][m]:
                return True
            elif target > matrix[mid][m]:
                l = m+1
            else:
                r = m-1

        return False
