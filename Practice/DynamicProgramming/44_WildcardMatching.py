# 44. Wildcard Matching
# Solved
# Hard
# Topics
# Companies
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

# Constraints:

# 0 <= s.length, p.length <= 2000
# s contains only lowercase English letters.
# p contains only lowercase English letters, '?' or '*'.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(s)
        n=len(p)
        cache={}
        def rec(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            elif i>=m and j>=n:
                return True
            elif i>=m and j<n and p[j]=='*':
                cache[(i,j)]= rec(i,j+1)
                return cache[(i,j)]
            elif i>=m or j>=n:
                return False
            elif p[j]=='*': 
                cache[(i,j)]= rec(i,j+1) or rec(i+1,j+1) or rec(i+1,j)
                return cache[(i,j)]
            elif s[i]==p[j] or p[j]=='?':
                cache[(i,j)]= rec(i+1,j+1)
                return cache[(i,j)]

            return False
        

        return rec(0,0)