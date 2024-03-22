# 542. 01 Matrix
# Solved
# Medium
# Topics
# Companies
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.


# Example 1:


# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:


# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]


# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        res = [[-1 for _ in range(n)] for _ in range(m)]

        q = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    visited.add((i, j))

        rowM = [-1, +1, 0, 0]
        colM = [0, 0, -1, +1]
        while q:
            curr = q.popleft()
            r = curr[0]
            c = curr[1]
            res[r][c] = curr[2]

            for i in range(4):
                nRow = r+rowM[i]
                nCol = c+colM[i]
                if nRow >= 0 and nCol >= 0 and nRow < m and nCol < n and (nRow, nCol) not in visited:
                    q.append((nRow, nCol, curr[2]+1))
                    visited.add((nRow, nCol))

        return res
