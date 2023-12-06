# 217. Contains Duplicate
# Easy
# 11.1K
# 1.2K
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# Accepted
# 3.4M
# Submissions
# 5.5M
# Acceptance Rate
# 61.1%
# Seen this question in a real interview before?
# 1/4

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache=set()
        for num in nums:
            if num in cache:
                return True
            cache.add(num)
        return False


        