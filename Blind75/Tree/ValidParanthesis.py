# 20. Valid Parentheses
# Easy
# 23K
# 1.6K
# Companies
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
        st = deque()

        for i, c in enumerate(s):
            if c == '{' or c == '[' or c == '(':
                st.append(c)
            else:
                if len(st) == 0:
                    return False
                val = st.pop()
                if (c == '}' and val == '{') or (c == ')' and val == '(') or (c == ']' and val == '['):
                    continue
                return False

        return True if len(st) == 0 else False
