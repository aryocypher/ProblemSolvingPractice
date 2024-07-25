# 300. Longest Increasing Subsequence
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
 

# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        cache={}
        def rec(i,prev):
            if i>=n:
                return 0
            if (i,prev) in cache:
                return cache[(i,prev)]
            inc=0
            exc=0

            if nums[i]>prev:
                inc=1+rec(i+1,nums[i])
            
            exc=rec(i+1,prev)
            cache[(i,prev)]= max(inc,exc)
            return cache[(i,prev)]

        return rec(0,-sys.maxsize)
        

    #Neetcode solution:- Elegant
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        vals=[1]*(n)

        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    vals[i]=max(vals[i],vals[j]+1)

        return max(vals)