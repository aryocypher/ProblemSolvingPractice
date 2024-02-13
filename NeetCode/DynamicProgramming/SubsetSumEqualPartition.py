# 416. Partition Equal Subset Sum
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.


# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.


# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for num in nums:
            sum += num

        if sum % 2 == 1:
            return False

        sum = sum//2

        cache = []

        for i in range(len(nums)):
            curr = [-1]*(sum+1)
            cache.append(curr)
            cache[i][0] = 0

        def rec(amount, i):
            if amount == 0:
                return 1
            if i >= len(nums):
                return 0
            if cache[i][amount] != -1:
                return cache[i][amount]
            inc = 0
            exc = 0
            if amount >= nums[i]:
                inc = rec(amount-nums[i], i+1)
            exc = rec(amount, i+1)

            cache[i][amount] = max(inc, exc)

            return cache[i][amount]

        return rec(sum, 0)
