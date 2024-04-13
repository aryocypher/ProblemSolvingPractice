# 131. Palindrome Partitioning
# Medium
# Topics
# Companies
# Given a string s, partition s such that every 
# substring
#  of the partition is a 
# palindrome
# . Return all possible palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]
 

# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.
class Solution:
    def isPalindrome(self,i,j,s):
        while i<j:
            if s[i]!=s[j]:
                return False
            i,j=i+1,j-1

        return True

    def partition(self, s: str) -> List[List[str]]:
        res=[]
        curr=[]

        def dfs(i):
            if i==len(s):
                res.append(curr[:])
            for j in range(i,len(s)):
                if self.isPalindrome(s,i,j):
                    curr.append(s[i:j+1])
                    dfs(j+1)
                    curr.pop()
        
        dfs(0)
        return res
            