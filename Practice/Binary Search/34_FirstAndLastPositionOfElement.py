# 34. Find First and Last Position of Element in Sorted Array
# Solved
# Medium
# Topics
# Companies
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109


class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstOccurence():
            l=0
            r=len(nums)-1
            res=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    res=mid
                    r=mid-1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return res

        def lastOccurence():
            l=0
            r=len(nums)-1
            res=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    res=mid
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return res

        targetIndexes=[]
        targetIndexes.append(firstOccurence())
        targetIndexes.append(lastOccurence())

        return targetIndexes
                


        