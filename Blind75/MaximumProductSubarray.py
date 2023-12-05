# 152. Maximum Product Subarray
# Medium
# 17.7K
# 563
# Companies
# Given an integer array nums, find a
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.


# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1

        maxProd = -sys.maxsize-1

        for i in range(len(nums)-1):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix *= nums[i]
            suffix *= nums[len(nums)-1-i]
            maxProd = max(prefix, suffix, maxProd)

        return maxProd
