# 239. Sliding Window Maximum
# Attempted
# Hard
# Topics
# Companies
# Hint
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.


# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def findHighest(l, r):
            maxVal = nums[l]
            for i in range(l, r):
                maxVal = max(maxVal, nums[i])
            return maxVal

        l = 0
        r = k
        n = len(nums)
        res = []
        maxVal = findHighest(l, r)
        res.append(maxVal)
        while r < n:
            l += 1
            if maxVal == nums[l-1]:
                maxVal = findHighest(l, r)
            maxVal = max(maxVal, nums[r])
            r += 1
            res.append(maxVal)

        return res
