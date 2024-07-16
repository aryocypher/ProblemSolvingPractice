# 188. Best Time to Buy and Sell Stock IV
# Solved
# Hard
# Topics
# Companies
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# Example 2:

# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

# Constraints:

# 1 <= k <= 100
# 1 <= prices.length <= 1000
# 0 <= prices[i] <= 1000
class Solution:
    def maxProfit(self, l: int, prices: List[int]) -> int:
        n=len(prices)
        cache=[[[0 for a in range(l+1)] for b in range(2)] for c in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(0,2):
                for k in range(1,l+1):
                    if j==0:
                        cache[i][j][k]=max(-prices[i]+cache[i+1][1][k],cache[i+1][0][k])
                    else:
                        cache[i][j][k]=max(prices[i]+cache[i+1][0][k-1],cache[i+1][1][k])

        return cache[0][0][l]