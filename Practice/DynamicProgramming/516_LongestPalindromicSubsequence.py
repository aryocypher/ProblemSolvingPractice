# 516. Longest Palindromic Subsequence
# Solved
# Medium
# Topics
# Companies
# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
# Example 2:

# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists only of lowercase English letters.
class Solution:
    #Reverse a string
    def longestPalindromeSubseq(self, s: str) -> int:
        t=s[::-1]
        n=len(s)
        prev=[0]*(n+1)

        for i in range(1,n+1):
            curr=[0]*(n+1)
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    curr[j]=1+prev[j-1]
                else:
                    curr[j]=max(curr[j-1],prev[j])
            prev=curr
            print(prev)

        return prev[n]    

    def longestPalindromeSubseqRec(self, s: str) -> int:
        t=s[::-1]
        n=len(s)
        cache={}
        def rec(i,j):
            if i>=n or j>=n:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            if s[i]==t[j]:
                cache[(i,j)]= 1+rec(i+1,j+1)
                return cache[(i,j)]

            l=rec(i+1,j)
            r=rec(i,j+1)

            cache[(i,j)]= max(l,r)
            return cache[(i,j)]

        return rec(0,0)