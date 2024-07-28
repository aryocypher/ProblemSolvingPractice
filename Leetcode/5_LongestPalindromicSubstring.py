# 5. Longest Palindromic Substring
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxL=0
        maxR=0

        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l)>(maxR-maxL):
                    maxR=r
                    maxL=l
                r=r+1
                l=l-1

            l=i
            r=i-1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l)>(maxR-maxL):
                    maxR=r
                    maxL=l
                r=r+1
                l=l-1
                

        return s[maxL:maxR+1]
