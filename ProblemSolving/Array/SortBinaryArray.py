'''

Given a binary array, in-place sort it in linear time and constant space. The output should contain all zeroes, followed by all ones.

Input : [1, 0, 1, 0, 1, 0, 0, 1]
Output: [0, 0, 0, 0, 1, 1, 1, 1]

Input : [1, 1]
Output: [1, 1]

'''


class Solution:
    def sortArray(self, nums: List[int]) -> None:
        # Write your code here...
        index = 0
        end = len(nums)-1
        while (index < end):
            if (nums[index] == 1):
                nums[index], nums[end] = nums[end], nums[index]
                end = end-1
                continue
            index += 1
        return
