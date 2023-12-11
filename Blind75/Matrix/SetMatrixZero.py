# 73. Set Matrix Zeroes
# Medium
# 13.6K
# 680
# Companies
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.


# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1


# Follow up:

# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


class Solution:
    # use this method
    def setZeroesWithConstantSpace(self, matrix: List[List[int]]) -> None:
        rowZero = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        rowZero = True
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if (matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        if rowZero == True:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if (matrix[i][j] == 0):
                    res.append([i, j])

        for k in range(len(res)):
            for i in range(len(matrix)):
                matrix[i][res[k][1]] = 0

            for j in range(len(matrix[0])):
                matrix[res[k][0]][j] = 0
