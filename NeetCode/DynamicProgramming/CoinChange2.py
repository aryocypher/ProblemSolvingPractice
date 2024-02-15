# 518. Coin Change II
# Solved
# Medium
# Topics
# Companies
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.


# Example 1:

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:

# Input: amount = 10, coins = [10]
# Output: 1

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        cache = []

        for i in range(amount+1):
            curr = [-1]*(len(coins)+1)
            cache.append(curr)

        def dfs(val, i):

            if val == 0:
                return 1
            if i >= n:
                return 0
            if cache[val][i] != -1:
                return cache[val][i]
            c1 = 0
            c2 = 0
            if val >= coins[i]:
                c1 = dfs(val-coins[i], i)
            c2 = dfs(val, i+1)

            cache[val][i] = c1+c2
            return cache[val][i]

        return dfs(amount, 0)
