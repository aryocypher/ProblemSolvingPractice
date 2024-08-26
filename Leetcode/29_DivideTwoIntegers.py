# 29. Divide Two Integers
# Solved
# Medium
# Topics
# Companies
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

# Constraints:

# -231 <= dividend, divisor <= 231 - 1
# divisor != 0
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==divisor:
            return 1
        
        cnt=0

        isSigned=False

        isSigned= True if dividend<0 else False
        isSigned= not isSigned if divisor<0 else isSigned
        n=abs(dividend)
        d=abs(divisor)
        q=0
        
        while n>=d:
            cnt=0
            while n>=(d<<(cnt+1)):
                cnt+=1
            q+=(1<<cnt)
            n-=d<<(cnt)

        if q>=(1<<31):
            if isSigned:
                return -1*(1<<31)
            else:
                return (1<<31)-1

        return -1*q if isSigned else q
            

        

