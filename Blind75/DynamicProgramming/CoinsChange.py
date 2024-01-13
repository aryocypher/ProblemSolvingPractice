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
    def coinChangeRecWay(self, coins: List[int], amount: int) -> int:
        cache = [-2]*(amount+1)

        def coinChangeRec(val):
            if val == 0:
                return 0

            if cache[val] != -2:
                return cache[val]

            canCoinBeUsed = False
            coinsCount = []

            for coin in coins:
                # if coin==amount:
                #     cache[val]=1
                #     return cache[val]

                if coin <= val:
                    newVal = val-coin
                    demCount = coinChangeRec(newVal)
                    if demCount != -1:
                        canCoinBeUsed = True
                        coinsCount.append(demCount)

            cache[val] = min(coinsCount)+1 if canCoinBeUsed else -1
            return cache[val]

        return coinChangeRec(amount)

    # VeryImp
    def coinChangeIte(self, coins: List[int], amount: int) -> int:
        cache = [amount+1]*(amount+1)

        for val in range(amount+1):
            if val == 0:
                cache[val] = 0

            for coin in coins:
                if val-coin >= 0:
                    cache[val] = min(cache[val], cache[val-coin]+1)

        return cache[amount] if cache[amount] != amount+1 else -1
