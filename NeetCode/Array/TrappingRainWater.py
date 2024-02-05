# 42. Trapping Rain Water
# Solved
# Hard
# Topics
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = [], [0]*len(height)
        for i in range(len(height)):
            if i == 0:
                left.append(height[0])
            else:
                left.append(max(left[i-1], height[i]))

        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                right[i] = height[i]
            else:
                right[i] = max(right[i+1], height[i])

        count = 0

        for i in range(1, len(height)-1):
            curr = min(left[i-1], right[i+1])-height[i]
            if curr > 0:
                count += curr

        return count
