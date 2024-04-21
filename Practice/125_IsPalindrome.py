# 125. Valid Palindrome
# Solved
# Easy
# Topics
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


class Solution:
    def isAlphabetChar(self,c:str)->bool:
        val=ord(c)
        if (val>=ord('a') and val<=ord('z')) or (val>=ord('A') and val<=ord('Z')):
            return True
        
        return False

    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return True        

        def rec(i,j):
            print(i,j,s[i],s[j],self.isAlphabetChar(s[i]),self.isAlphabetChar(s[j]))
            if i>=j:
                return True

            if not self.isAlphabetChar(s[i]):
                return rec(i+1,j)
            if not self.isAlphabetChar(s[j]):
                return rec(i,j-1)

            if s[i].lower()==s[j].lower():
                return rec(i+1,j-1)

            return False
        
        return rec(0,len(s)-1)

            

        