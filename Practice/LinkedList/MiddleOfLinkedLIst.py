# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hop = head
        hopTwice = head

        while hopTwice.next and hopTwice.next.next:
            hop = hop.next
            hopTwice = hopTwice.next.next

        return hop.next if hopTwice.next else hop
