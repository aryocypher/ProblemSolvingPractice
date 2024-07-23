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
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        cache={}
        def rec(i,j):
            if i>=m or j>=n:
                return 0

            if(i,j) in cache:
                return cache[(i,j)]

            if j==n-1 and s[i]==t[j]:
                cache[(i,j)]= 1+rec(i+1,j)
                return cache[(i,j)]
            
            inc=0
            exc=0
            if s[i]==t[j]:
                inc=rec(i+1,j+1)

            exc=rec(i+1,j)
            cache[(i,j)]= inc+exc
            return cache[(i,j)]
        

        return rec(0,0)
                