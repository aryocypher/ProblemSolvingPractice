# 115. Distinct Subsequences
# Solved
# Hard
# Topics
# Companies
# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.


# Example 1:

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
# Example 2:

# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag


# Constraints:

# 1 <= s.length, t.length <= 1000
# s and t consist of English letters.

class Solution:
    def numDistinctIt(self, s: str, t: str) -> int:
        sL = len(s)
        tL = len(t)
        cache = [[-1 for _ in range(tL+1)] for _ in range(sL+1)]

        def dfs(i, j):
            if j == tL:
                return 1
            if i >= sL:
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            inc = 0
            exc = 0
            if s[i] == t[j]:
                inc = dfs(i+1, j+1)
            exc = dfs(i+1, j)
            cache[i][j] = inc+exc
            return cache[i][j]

        return dfs(0, 0)

    def numDistinct(self, s: str, t: str) -> int:
        sL = len(s)
        tL = len(t)
        cache = [[-1 for _ in range(tL+1)] for _ in range(sL+1)]

        def dfs(i, j):
            if i >= sL or j >= tL:
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            inc1 = 0
            inc = 0
            exc = 0
            if s[i] == t[j] and j == tL-1:
                inc1 = 1
            elif s[i] == t[j]:
                inc = dfs(i+1, j+1)
            exc = dfs(i+1, j)
            cache[i][j] = inc1+inc+exc
            return cache[i][j]

        return dfs(0, 0)
