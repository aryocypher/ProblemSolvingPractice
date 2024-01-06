# 5. Longest Palindromic Substring
# Medium
# 28.4K
# 1.7K
# Companies
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

        longestPalindromeStart = 0
        longestPalindromeEnd = 0
        longestPalindromeSize = 0
        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l = l-1
                r = r+1

            if (r-l+1) > longestPalindromeSize:
                longestPalindromeStart = l+1
                longestPalindromeEnd = r
                longestPalindromeSize = r-l+1

            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l = l-1
                r = r+1

            if (r-l+1) > longestPalindromeSize:
                longestPalindromeStart = l+1
                longestPalindromeEnd = r
                longestPalindromeSize = r-l+1

        return s[longestPalindromeStart:longestPalindromeEnd]
