# Number Spiral
# A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:

# Your task is to find out the number in row y and column x.
# Input
# The first input line contains an integer t: the number of tests.
# After this, there are t lines, each containing integers y and x.
# Output
# For each test, print the number in row y and column x.
# Constraints

# 1 \le t \le 10^5
# 1 \le y,x \le 10^9

# Example
# Input:
# 3
# 2 3
# 1 1
# 4 2

# Output:
# 8
# 1
# 15

def calculateSpiralValue(a:int,b:int):
    if a>=b:
        if a%2==0:
            return (a*a)-(b-1)
        else:
            return (a*a)-(a-1)-(a-b)
    else:
        if b%2==1:
            return (b*b)-(a-1)
        else:
            return (b*b)-(b-1)-(b-a)


num= int(input())
i=0
while i<num:
    i+=1
    vals=input()
    valList=vals.split()
    print(calculateSpiralValue(int(valList[0]),int(valList[1])))


