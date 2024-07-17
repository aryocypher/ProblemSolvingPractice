# Subset Sum Problem
# Difficulty: MediumAccuracy: 32.0%Submissions: 228K+Points: 4
# Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 


# Example 1:

# Input:
# N = 6
# arr[] = {3, 34, 4, 12, 5, 2}
# sum = 9
# Output: 1 
# Explanation: Here there exists a subset with
# sum = 9, 4+3+2 = 9.
# Example 2:

# Input:
# N = 6
# arr[] = {3, 34, 4, 12, 5, 2}
# sum = 30
# Output: 0 
# Explanation: There is no subset with sum 30.

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function isSubsetSum() which takes the array arr[], its size N and an integer sum as input parameters and returns boolean value true if there exists a subset with given sum and false otherwise.
# The driver code itself prints 1, if returned value is true and prints 0 if returned value is false.
 

# Expected Time Complexity: O(sum*N)
# Expected Auxiliary Space: O(sum*N)
 

# Constraints:
# 1 <= N <= 100
# 1<= arr[i] <= 100
# 1<= sum <= 104
class Solution:
    #Most optimal apporach
    def isSubsetSum (self, N, arr, sum):
        cache=[0 for i in range(sum+1)]
        cache[0]=1
        
        for i in range(1,N+1):
            curr=[0]*(sum+1)
            curr[0]=1
            for j in range(1,sum+1):
                inc=False
                exc=False
                if arr[i-1]<=j:
                    inc=cache[j-arr[i-1]]
                exc=cache[j]
                curr[j]=inc or exc
                
            cache=curr
        return cache[sum]
    def isSubsetSumIterative(self, N, arr, sum):
        cache=[[0 for i in range(sum+1)] for j in range(N+1)]
        
        for i in range(N+1):
            cache[i][0]=True
            
        
        for i in range(1,N+1):
            for j in range(1,sum+1):
                inc=False
                exc=False
                if arr[i-1]<=j:
                    inc=cache[i-1][j-arr[i-1]]
                exc=cache[i-1][j]
                cache[i][j]=inc or exc
                
        
        return cache[N][sum]
                
    def isSubsetSumRec(self, N, arr, sum):
        cache={}
        
        def rec(i,val):
            if val==0:
                return True
            if i>=N or val<0:
                return False
            inc=False
            exc=False
            if (i,val) in cache:
                return cache[(i,val)]
            if val>=arr[i]:
                inc=rec(i+1,val-arr[i])
                
            exc=rec(i+1,val)
            
            cache[(i,val)]= inc or exc
            return cache[(i,val)]
            
        return rec(0,sum)
