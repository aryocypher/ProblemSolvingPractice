# 25. Reverse Nodes in k-Group
# Solved
# Hard
# Topics
# Companies
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
 

# Follow-up: Can you solve the problem in O(1) extra memory space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseGroup(self,head,tail):
        curr=head
        prev=None
        while curr!=tail:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        
        curr.next=prev
        print(curr.val,head.val)
        return [curr,head]

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i=0
        dummy=ListNode(0,head)
        curr=dummy

        while curr:
            temp=curr
            while i<k and curr.next:
                curr=curr.next
                i+=1
            if i==k:
                next=curr.next
                val=self.reverseGroup(temp.next,curr)
                temp.next=val[0]
                val[1].next=next
                curr=val[1]
                i=0
            else:
                break

        
        return dummy.next