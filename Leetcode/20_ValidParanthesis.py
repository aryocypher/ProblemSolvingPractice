# 20. Valid Parentheses
# Solved
# Easy
# Topics
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()

        for c in s:
            if c=='{' or c=='[' or c=='(':
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                val=stack.pop()
                if (c=='}' and val=='{') or (c==')' and val=='(') or (c==']' and val=='['):
                    continue
                else:
                    return False

        return True if len(stack)==0 else False
