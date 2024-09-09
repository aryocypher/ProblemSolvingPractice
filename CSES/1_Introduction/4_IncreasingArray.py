# Increasing Array
# Time limit: 2.00 s
# Memory limit: 512 MB



# You are given an array of n integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.
# On each move, you may increase the value of any element by one. What is the minimum number of moves required?
# Input
# The first input line contains an integer n: the size of the array.
# Then, the second line contains n integers x_1,x_2,\ldots,x_n: the contents of the array.
# Output
# Print the minimum number of moves.
# Constraints

# 1 \le n \le 2 \cdot 10^5
# 1 \le x_i \le 10^9

# Example
# Input:
# 5
# 3 2 5 1 7

# Output:
# 5
inputNum=input()
numsInput= input()   # takes the whole line of n numbers
nums = list(map(int,numsInput.split(' ')))
count=0
maxVal=nums[0]
for num in nums:
    if num<maxVal:
        count+=maxVal-num
    maxVal=max(num,maxVal)

print(count)

