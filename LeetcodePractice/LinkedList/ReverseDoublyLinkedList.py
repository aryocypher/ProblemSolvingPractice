# User function Template for python3

'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
'''


from collections import deque


class Solution:
    def reverseDLL(self, head):
        # return head after reversing
        prev = None
        curr = head
        q = deque()
        q.appe

        while curr:
            next = curr.next
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next

        return prev
