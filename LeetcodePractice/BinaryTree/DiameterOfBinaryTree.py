 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterAndHeightOfBinaryTree(self,root:Optional[TreeNode]):
        if root==None:
            return [0,0]
        left=self.diameterAndHeightOfBinaryTree(root.left)
        right=self.diameterAndHeightOfBinaryTree(root.right)
        height=max(left[0],right[0])+1
        diameter =max(left[0]+right[0]+1,left[1],right[1])
        return [height,diameter]


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res= self.diameterAndHeightOfBinaryTree(root)
        return res[1]-1