# 22. Generate Parentheses
# Solved
# Medium
# Topics
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


# Constraints:

# 1 <= n <= 8
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st = []
        res = []

        def generate(open, close):
            if open == close == n:
                res.append("".join(st))
            if open < n:
                st.append('(')
                generate(open+1, close)
                st.pop()
            if close < open:
                st.append(')')
                generate(open, close+1)
                st.pop()

        generate(0, 0)
        return res
