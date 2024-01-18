# 198. House Robber
# Solved
# Medium
# Topics
# Companies
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.


# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400


class Solution:
    def robRecursive(self, nums: List[int]) -> int:
        cache = [-1]*len(nums)
        numsLen = len(nums)

        def robRec(i):
            if i >= numsLen:
                return 0
            if cache[i] != -1:
                return cache[i]
            val = nums[i]

            inc = robRec(i+2)
            exc = robRec(i+1)

            cache[i] = max(val+inc, exc)
            return cache[i]

        return robRec(0)

    def robIterative(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cache = [0]*len(nums)
        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])

        for i in range(2, len(cache)):
            cache[i] = max(nums[i]+cache[i-2], cache[i-1])
        return cache[len(nums)-1]
