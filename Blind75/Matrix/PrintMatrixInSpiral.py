# 54. Spiral Matrix
# Medium
# 13.9K
# 1.2K
# Companies
# Given an m x n matrix, return all elements of the matrix in spiral order.


# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1

        while (top <= bottom and left <= right):
            # For moving left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])

            top += 1

            # For moving top to bottom.
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])

            right -= 1

            # For moving right to left.
            if (top <= bottom):
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])

                bottom -= 1

            # For moving bottom to top.
            if (left <= right):
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])

                left += 1

        return res
