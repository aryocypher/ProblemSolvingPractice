# 18. 4Sum
# Solved
# Medium
# Topics
# Companies
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 

# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j!=i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=n-1
                while k<l:
                    if nums[i]+nums[j]+nums[k]+nums[l]==target:
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                    elif nums[i]+nums[j]+nums[k]+nums[l]>target:
                        l-=1
                    else:
                        k+=1
        
        return res

