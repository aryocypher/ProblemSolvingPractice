class Solution:
    def getHighestAndSecondHighest(self, nums: List[int]):
        highestNum = nums[0]
        secondHighestNum = nums[1]
        if (secondHighestNum > highestNum):
            highestNum, secondHighestNum = secondHighestNum, highestNum

        for i in range(2, len(nums)):
            num = nums[i]
            if (num > highestNum):
                highestNum, secondHighestNum = num, highestNum
            elif (num > secondHighestNum):
                secondHighestNum = num

        return [highestNum, secondHighestNum]

    def getLowestAndSecondLowest(self, nums: List[int]):
        indices = set()
        lowestNum = nums[0]
        secondLowestNum = nums[1]
        if (secondLowestNum < lowestNum):
            lowestNum, secondLowestNum = secondLowestNum, lowestNum

        for i in range(2, len(nums)):
            num = nums[i]
            if (num < lowestNum):
                lowestNum, secondLowestNum = num, lowestNum
            elif (num < secondLowestNum):
                secondLowestNum = num

        return [lowestNum, secondLowestNum]

    def maxProduct(self, nums: List[int]) -> int:
        highestNum, secondHighestNum = self.getHighestAndSecondHighest(nums)
        lowestNum, secondLowestNum = self.getLowestAndSecondLowest(nums)
        return max(int((highestNum-1)*(secondHighestNum-1)), int((lowestNum-1)*(secondLowestNum-1)))
