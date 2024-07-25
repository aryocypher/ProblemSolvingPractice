# 673. Number of Longest Increasing Subsequence
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, return the number of longest increasing subsequences.

# Notice that the sequence has to be strictly increasing.

 

# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:

# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
 

# Constraints:

# 1 <= nums.length <= 2000
# -106 <= nums[i] <= 106
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        cache=[[1 for i in range(2)] for i in range(n)]

        
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    if cache[i][0]==cache[j][0]+1:
                        cache[i][1]+=cache[j][1]
                    elif cache[j][0]+1>cache[i][0]:
                        cache[i][0]=cache[j][0]+1
                        cache[i][1]=cache[j][1]
 


        maxVal=0
        freq=0
        for i in range(n):
            if cache[i][0]==maxVal:
                freq+=cache[i][1]
            if cache[i][0]>maxVal:
                maxVal=cache[i][0]
                freq=cache[i][1]
        
        return freq