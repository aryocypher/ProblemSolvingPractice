# Longest Sub-Array with Sum K
# Difficulty: MediumAccuracy: 24.64%Submissions: 284K+Points: 4
# Given an array containing N integers and an integer K., Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value K.

 

# Example 1:
 

# Input :
# A[] = {10, 5, 2, 7, 1, 9}
# K = 15
# Output : 4
# Explanation:
# The sub-array is {5, 2, 7, 1}.
# Example 2:

# Input : 
# A[] = {-1, 2, 3}
# K = 6
# Output : 0
# Explanation: 
# There is no such sub-array with sum 6.
# Your Task:
# This is a function problem. The input is already taken care of by the driver code. You only need to complete the function lenOfLongSubarr() that takes an array (A), sizeOfArray (n),  sum (K)and returns the required length of the longest Sub-Array. The driver code takes care of the printing.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N).

 

# Constraints:
# 1<=N<=105
# -105<=A[i], K<=105
 


#User function Template for python3



class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        cache={}
        currSum=0
        cache[0]=-1
        largestLength=0
        for i in range(n):
            currSum+=arr[i]
            if currSum-k in cache:
                largestLength=max(largestLength,i-cache[currSum-k])
            if currSum not in cache:
                cache[currSum]=i
                
        
        return largestLength
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends