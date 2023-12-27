# 206. Reverse Linked List
# Easy
# 20.2K
# 376
# Companies
# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []


# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseListRec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        rest = self.reverseListRec(head.next)
        head.next.next = head
        head.next = None
        return rest

    def reverseListIte(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head != None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
