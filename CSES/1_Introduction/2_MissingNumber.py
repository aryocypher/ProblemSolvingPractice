#missing Number
# You are given all numbers between 1,2,\ldots,n except one. Your task is to find the missing number.
# Input
# The first input line contains an integer n.
# The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
# Output
# Print the missing number.
# Constraints

# 2 \le n \le 2 \cdot 10^5

# Example
# Input:
# 5
# 2 3 1 5

# Output:
# 4

n=int(input())
res=0
numsInput= input()   # takes the whole line of n numbers
nums = list(map(int,numsInput.split(' ')))
nums.append(0)
for i,num in enumerate(nums):
    res=res^i^num

res=res^len(nums)
print(res)
