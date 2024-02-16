
# Code
# Testcase
# Testcase
# Test Result
# 97. Interleaving String
# Solved
# Medium
# Topics
# Companies
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where s and t are divided into n and m
# substrings
#  respectively, such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.


# Example 1:


# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.
# Example 2:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
# Example 3:

# Input: s1 = "", s2 = "", s3 = ""
# Output: true
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1L = len(s1)
        s2L = len(s2)
        s3L = len(s3)

        if s1L > s3L or s2L > s3L or s1L+s2L > s3L:
            return False

        cache = [[[-1 for _ in range(s3L+1)]
                  for _ in range(s2L+1)] for _ in range(s1L+1)]

        def rec(i, j, k):

            if k >= s3L and i >= s1L and j >= s2L:
                return True
            if k >= s3L:
                return False

            if cache[i][j][k] != -1:
                return cache[i][j][k]

            if i < s1L and j < s2L:
                if s1[i] == s3[k] and s2[j] == s3[k]:
                    cache[i][j][k] = rec(i+1, j, k+1) or rec(i, j+1, k+1)
                elif s1[i] == s3[k]:
                    cache[i][j][k] = rec(i+1, j, k+1)
                elif s2[j] == s3[k]:
                    cache[i][j][k] = rec(i, j+1, k+1)
                else:
                    cache[i][j][k] = False
            elif i < s1L:
                if s1[i] == s3[k]:
                    cache[i][j][k] = rec(i+1, j, k+1)
                else:
                    cache[i][j][k] = False
            elif j < s2L:
                if s2[j] == s3[k]:
                    cache[i][j][k] = rec(i, j+1, k+1)
                else:
                    cache[i][j][k] = False
            else:
                cache[i][j][k] = False
            return cache[i][j][k]

        return rec(0, 0, 0)
