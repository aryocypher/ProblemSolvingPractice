# 79. Word Search
# Solved
# Medium
# Topics
# Companies
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
 

# Follow up: Could you use search pruning to make your solution faster with a larger board?
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r,c,w=len(board),len(board[0]),len(word)

        def dfs(i,j,k):
            nonlocal r,c,w
            if i<0 or j<0 or k>=w or i>=r or j>=c:
                return False
            
            if k==w-1 and board[i][j]==word[k]:
                return True
            
            temp=board[i][j]
            if board[i][j]==word[k]:
                print(board[i][j])
                board[i][j]="."
                left=dfs(i,j-1,k+1)
                right=dfs(i,j+1,k+1)
                top=dfs(i-1,j,k+1)
                bottom=dfs(i+1,j,k+1)
                board[i][j]=temp
                return left or right or top or bottom
            
            return False
        
        for i in range(r):
            for j in range(c):
                if dfs(i,j,0):
                    return True
        
        return False