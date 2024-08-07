# 14. Longest Common Prefix
# Solved
# Easy
# Topics
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        resL=0

        for i in range(len(strs[0])):
            for s in strs:
                if i==len(s) or strs[0][i]!=s[i]:
                    return s[0:resL] 
            resL+=1


        return strs[0][0:resL] 