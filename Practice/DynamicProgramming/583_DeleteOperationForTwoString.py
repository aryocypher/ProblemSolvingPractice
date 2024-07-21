# 583. Delete Operation for Two Strings
# Solved
# Medium
# Topics
# Companies
# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

# In one step, you can delete exactly one character in either string.

 

# Example 1:

# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# Example 2:

# Input: word1 = "leetcode", word2 = "etco"
# Output: 4
 

# Constraints:

# 1 <= word1.length, word2.length <= 500
# word1 and word2 consist of only lowercase English letters.
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        prev=[0]*(n+1)

        for i in range(1,m+1):
            curr=[0]*(n+1)
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    curr[j]=1+prev[j-1]
                else:
                    curr[j]=max(curr[j-1],prev[j])
            prev=curr

        return (n-prev[n])+(m-prev[n])