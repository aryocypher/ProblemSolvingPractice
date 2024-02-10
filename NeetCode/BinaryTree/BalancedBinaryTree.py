# 110. Balanced Binary Tree
# Solved
# Easy
# Topics
# Companies
# Given a binary tree, determine if it is
# height-balanced
# .


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true


# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def isBalancedRec(node):
            if node == None:
                return [0, True]

            left = isBalancedRec(node.left)
            right = isBalancedRec(node.right)

            if not left[1] or not right[1]:
                return [0, False]

            diff = abs(left[0]-right[0])

            if diff > 1:
                return [0, False]

            val = [max(left[0], right[0])+1, True]
            return val

        return isBalancedRec(root)[1]
