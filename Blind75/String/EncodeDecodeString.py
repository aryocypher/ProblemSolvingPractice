# 659 · Encode and Decode Strings
# Algorithms
# Medium
# Accepted Rate
# 65%

# Description
# Solution53
# Notes
# Discuss99+
# Leaderboard
# Record
# Description
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode


# Example
# Example1

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"
# Example2

# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        res = ""
        for word in strs:
            res += word+":;"
        print(res)
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        if str == None:
            return False
        # write your code here
        res = str.split(":;")
        return res[0:len(res)-1]
