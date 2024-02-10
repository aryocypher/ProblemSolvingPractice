# 226. Invert Binary Tree
# Easy
# 13.5K
# 196
# Companies
# Given the root of a binary tree, invert the tree, and return its root.


# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []


# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTreeIterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        q = deque()
        q.append(root)

        while (len(q) > 0):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            node.left, node.right = node.right, node.left

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left
        return root
