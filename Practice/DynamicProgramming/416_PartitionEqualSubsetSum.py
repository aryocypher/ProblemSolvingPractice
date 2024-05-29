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
        numsSum=sum(nums)
        n=len(nums)
        if numsSum%2!=0:
            return False
        numsSum=numsSum//2
        cache=[[False for i in range(numsSum+1)] for j in range(n+1)]
        
        for i in range(0,n+1):
            cache[i][0]=True

        for i in range(1,n+1):
            for j in range(1,numsSum+1):
                inc=False
                exc=False
                if nums[i-1]<=j:
                    inc=cache[i-1][j-nums[i-1]]
                exc=cache[i-1][j]
                cache[i][j]=inc or exc


        return cache[n][numsSum]


        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numsSum=sum(nums)
        n=len(nums)
        if numsSum%2!=0:
            return False
        cache=[[-1 for i in range(numsSum+1)] for j in range(n+1)]
        def rec(i,target):
            if target==0:
                return True
            if i==len(nums):
                return False
            if cache[i][target]!=-1:
                return cache[i][target]
            inc=False
            exc=False
            if nums[i]<=target:
                inc=rec(i+1,target-nums[i])
            exc=rec(i+1,target)
            cache[i][target]= inc or exc
            return cache[i][target]
        
        return rec(0,numsSum//2)

        