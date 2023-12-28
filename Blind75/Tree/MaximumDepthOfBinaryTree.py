# 104. Maximum Depth of Binary Tree
# Easy
# 12.3K
# 204
# Companies
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2


# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepthRec(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left = self.maxDepthRec(root.left)
        right = self.maxDepthRec(root.right)

        return max(left, right)+1

    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        q = deque()
        q.append(root)
        count = 0
        while len(q) != 0:
            count += 1
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return count
