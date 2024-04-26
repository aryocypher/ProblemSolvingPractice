# 560. Subarray Sum Equals K
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i=0
        
        for i in range(len(nums)):
            if i==0:
                continue
            nums[i]+=nums[i-1]
        
        cache=defaultdict(int)
        cache[0]=1
        count=0
        for num in nums:
            if num-k in cache:
                count+=cache[num-k]
            cache[num]+=1

        return count




        
