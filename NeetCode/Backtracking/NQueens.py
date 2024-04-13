# 51. N-Queens
# Solved
# Hard
# Topics
# Companies
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]
 

# Constraints:

# 1 <= n <= 9
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        posDiag=set()
        negDiag=set()
        res=[]
        board=[["."]*n for i in range(n)]
        
        def rec(r):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                posDiag.add((r+c))
                negDiag.add((r-c))
                col.add(c)
                board[r][c]="Q"
                rec(r+1)
                board[r][c]="."
                col.remove(c)
                negDiag.remove((r-c))
                posDiag.remove((r+c))

        rec(0)
        return res

        