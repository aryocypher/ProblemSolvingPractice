
from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = dict()
        for i, num in enumerate(nums):
            if target-num in res:
                return [i, res[target-num]]
            res[num] = i

        return None
