# 70. Climbing Stairs
# Solved
# Easy
# Topics
# Companies
# Hint
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    class Solution:

        def climbStairsIter(self, n: int) -> int:
            cache = [0, 1, 2]
            c = 3

            while (c <= n):
                cache.append(cache[c-1]+cache[c-2])
                c += 1

            return cache[n]

        def climbStairsRec(self, n: int) -> int:
            cache = [-1]*(n+1)

            def climbStairsRec(c):
                if c == 0:
                    return 1
                if cache[c] != -1:
                    return cache[c]
                c2 = 0
                c1 = 0
                if c > 1:
                    c2 = climbStairsRec(c-2)

                c1 = climbStairsRec(c-1)

                cache[c] = c2+c1

                return cache[c]

            return climbStairsRec(n)
