# 309. Best Time to Buy and Sell Stock with Cooldown
# Solved
# Medium
# Topics
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:

# Input: prices = [1]
# Output: 0
 

# Constraints:

# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000

class Solution:
    def maxProfitRec(self, prices: List[int]) -> int:
        cache={}
        n=len(prices)

        def rec(i,buy):
            if i>=n:
                return 0
            inc=0
            exc=0

            if (i,buy) in cache:
                return cache[(i,buy)]
            if buy:
                inc=-prices[i]+rec(i+1,not buy)
                exc=rec(i+1,buy)
            else:
                inc=prices[i]+rec(i+2,not buy)
                exc=rec(i+1,buy)

            cache[(i,buy)]= max(inc,exc)
            return cache[(i,buy)]

        return rec(0,1)
    

class Solution:
    def maxProfitIterative(self, prices: List[int]) -> int:
        n=len(prices)
        cache=[[0 for j in range(2)] for i in range(n+2)]

        for i in range(n-1,-1,-1):
            for j in range(2):
                inc=0
                exc=0
                if j==0:
                    inc=-prices[i]+cache[i+1][1]
                    exc=cache[i+1][0]
                else:
                    inc=prices[i]+cache[i+2][0]
                    exc=cache[i+1][1]
                cache[i][j]=max(inc,exc)

        return cache[0][0]
