# 238. Product of Array Except Self
# Medium
# 20.6K
# 1.2K
# Companies
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
class Solution:
    def productExceptSelfWithDivision(self, nums: List[int]) -> List[int]:
        contains_zero=False
        contains_non_zero=False
        mul_res=1
        res=[]
        for num in nums:
            if num==0:
                if(contains_zero==True):
                    mul_res=0
                contains_zero=True

            else:   
                contains_non_zero=True         
                mul_res*=num

        for num in nums:
            if num==0:
                if contains_non_zero==True:
                    res.append(mul_res)
                else:
                    res.append(0)
            else:
                if(contains_zero==True):
                    res.append(0)
                else:
                    res.append(int(mul_res/num))
        
        return res
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        product=1
        if (len(nums)==1):
            return nums
        for num in nums:
            product=product*num
            res.append(product)
        print(res)
        product=1
        for i in range(len(nums)-1,0,-1):
            res[i]=product*res[i-1]
            product*=nums[i]
        
        res[0]=product
        return res
        
        