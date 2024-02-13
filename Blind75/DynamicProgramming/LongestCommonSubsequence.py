# 1143. Longest Common Subsequence
# Solved
# Medium
# Topics
# Companies
# Hint
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.


# Example 1:

# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.


# Constraints:

# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[-1 for _ in range(len(text2) + 1)]
                 for _ in range(len(text1) + 1)]

        def lcsrec(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            if text1[i] == text2[j]:
                cache[i][j] = 1 + lcsrec(i + 1, j + 1)
            else:
                cache[i][j] = max(lcsrec(i+1, j), lcsrec(i, j + 1))

            return cache[i][j]

        return lcsrec(0, 0)

    def longestCommonSubsequenceIterative(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)

        cache = []

        for i in range(l1+1):
            curr = [0]*(l2+1)
            cache.append(curr)

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if text1[i-1] == text2[j-1]:
                    cache[i][j] = 1+cache[i-1][j-1]
                else:
                    cache[i][j] = max(cache[i][j-1], cache[i-1][j])

        return cache[l1][l2]
