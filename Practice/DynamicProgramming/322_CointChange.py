# 322. Coin Change
# Solved
# Medium
# Topics
# Companies
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104


class Solution:
    def coinChangeIterative(self, coins: List[int], amount: int) -> int:
        n=len(coins)

        cache=[[amount+1 for i in range(amount+1)] for j in range(n+1)]

        for i in range(n+1):
            cache[i][0]=0

        for i in range(1,n+1):
            for j in range(1,amount+1):
                inc=amount+1
                exc=amount+1

                if j>=coins[i-1]:
                    inc=1+cache[i][j-coins[i-1]]
                
                exc=cache[i-1][j]

                cache[i][j]=min(inc,exc)
        

        return -1 if cache[n][amount]>=amount+1 else cache[n][amount]
    
    def coinChangeRec(self, coins: List[int], amount: int) -> int:
        n=len(coins)

        cache={}
        def rec(i,currAmount):
            if currAmount==0:
                return 0
            if i>=n:
                return sys.maxsize
            if (i,currAmount) in cache:
                return cache[(i,currAmount)] 
            inc=sys.maxsize
            exc=sys.maxsize
            if currAmount>=coins[i]:
                inc=1+rec(i,currAmount-coins[i])
            exc=rec(i+1,currAmount)

            cache[(i,currAmount)]= min(inc,exc)
            return cache[(i,currAmount)]

        val=rec(0,amount)
        return -1 if val==sys.maxsize else val