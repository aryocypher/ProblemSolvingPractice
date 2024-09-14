# 4. Median of Two Sorted Arrays
# Solved
# Hard
# Topics
# Companies
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        total=len(A)+len(B)
        half=total//2
        if len(B)<len(A):
            B,A=A,B
        
        if total==1:
            return B[0]
        
        l,r=0,len(A)-1

        while True:
            i=(l + r)//2  # A
            j=half-i-2  # B
            print(i,j)

            Aleft=A[i] if i >= 0 else float("-infinity")
            Aright=A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft=B[j] if j >= 0 else float("-infinity")
            Bright=B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft<=Bright and Bleft<=Aright:
                #odd
                if total%2==1:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r=i-1
            else:
                l=i+1 
            
