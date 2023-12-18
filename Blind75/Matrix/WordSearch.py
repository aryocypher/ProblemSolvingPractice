# 79. Word Search
# Medium
# 14.7K
# 607
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
    def wordExist(self, board: List[List[str]], word: str, r,  c,  w) -> bool:
        if w == len(word):
            return True
        if r == len(board) or c == len(board[0]) or r < 0 or c < 0 or board[r][c] != word[w]:
            return False
        board[r][c] = "#"
        op1 = self.wordExist(board, word, r+1, c, w+1)
        op2 = self.wordExist(board, word, r, c+1, w+1)
        op3 = self.wordExist(board, word, r-1, c, w+1)
        op4 = self.wordExist(board, word, r, c-1, w+1)
        board[r][c] = word[w]

        return op1 or op2 or op3 or op4

    def exist(self, board: List[List[str]], word: str) -> bool:
        rSize = len(board)
        cSize = len(board[0])
        for i in range(rSize):
            for j in range(cSize):
                if (self.wordExist(board, word, i, j, 0)):
                    return True
        return False
