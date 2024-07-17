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
    #Space optimized tabulation
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        prev=[0]*(n+1)

        for i in range(1,m+1):
            curr=[0]*(n+1)
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    curr[j]=1+prev[j-1]
                else:
                    curr[j]=max(curr[j-1],prev[j])
            prev=curr

        return prev[n]
    def longestCommonSubsequenceIterative(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        cache=[[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    cache[i][j]=1+cache[i-1][j-1]
                else:
                    cache[i][j]=max(cache[i][j-1],cache[i-1][j])
        
        return cache[m][n]
    def longestCommonSubsequenceRec(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        cache={}
        def rec(i,j):
            if i>=m or j>=n:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            if text1[i]==text2[j]:
                cache[(i,j)]= 1+rec(i+1,j+1)
                return cache[(i,j)]
            l=rec(i+1,j)
            r=rec(i,j+1)
            cache[(i,j)]=max(l,r)
            return cache[(i,j)]

        return rec(0,0)
