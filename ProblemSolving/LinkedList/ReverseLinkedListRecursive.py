# Approach 1
# in this approach we return final element once and use the current node to manipulate pointers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rest


# Approach 2
# Having a global variable for node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return head
        resHead = head

        def reverseListRec(node: Optional[ListNode]):
            nonlocal resHead
            if (node.next == None):
                resHead = node
                return resHead
            res = reverseListRec(node.next)
            res.next = node
            return node

        node = reverseListRec(head)
        node.next = None

        return resHead

    # //Base condition
    # if(head==NULL || head->next==NULL) {
    #     return head;
    # }

    # node* newHead=recursiveReverse(head->next);
    # head->next->next=head;
    # head->next=NULL;

    # return newHead;
