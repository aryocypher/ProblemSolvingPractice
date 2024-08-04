# 24. Swap Nodes in Pairs
# Solved
# Medium
# Topics
# Companies
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:

# Input: head = []
# Output: []
# Example 3:

# Input: head = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairsSingleIteration(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        res=dummy
        curr =head
        while curr and curr.next:
            next=curr.next.next
            res.next=curr.next
            res.next.next=curr
            curr.next=None
            res=res.next.next
            curr=next

        if curr:
            res.next=curr

        return dummy.next
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l1=ListNode()
        l2=ListNode()
        l1Curr=l1
        l2Curr=l2
        curr=head
        isL1=True
        while curr:
            if isL1:
                l1Curr.next=curr
                l1Curr=l1Curr.next
                isL1=False
            else:
                l2Curr.next=curr
                l2Curr=l2Curr.next
                isL1=True
            curr=curr.next
        
        if l1Curr:
            l1Curr.next=None
        if l2Curr:
            l2Curr.next=None

        res=ListNode()
        curr=res

        l1Curr=l1.next
        l2Curr=l2.next

        while l1Curr and l2Curr:
            curr.next=l2Curr
            l2Curr=l2Curr.next
            curr=curr.next
            curr.next=l1Curr
            l1Curr=l1Curr.next
            curr=curr.next
            

        if l1Curr:
            curr.next=l1Curr
        
        if l2Curr:
            curr.next=l2Curr

        return res.next



