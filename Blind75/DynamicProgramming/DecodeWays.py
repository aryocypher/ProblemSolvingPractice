# 91. Decode Ways
# Solved
# Medium
# Topics
# Companies
# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The test cases are generated so that the answer fits in a 32-bit integer.


# Example 1:

# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# Example 3:

# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").


# Constraints:

# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

class Solution:
    def numDecodingsRecursive(self, s: str) -> int:
        sLen = len(s)
        cache = [-1]*len(s)

        def numDecRec(i):
            if i >= sLen:
                return 1
            if cache[i] != -1:
                return cache[i]

            if s[i] == '0':
                return 0

            val1 = numDecRec(i+1)
            val2 = 0
            if i != sLen-1:
                num = int(s[i:i+2])
                if num <= 26:
                    val2 = numDecRec(i+2)

            cache[i] = val1+val2
            return cache[i]

        return numDecRec(0)

    def numDecodingsIte(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1

        count1, count2 = 1, 1

        for i in range(1, len(s)):
            digit = int(s[i])
            digit2 = 10*(int(s[i-1]))+int(s[i])
            count = 0
            if digit > 0:
                count += count2
            if digit2 >= 10 and digit <= 26:
                count += count1

            count2, count1 = count, count2

        return count2
