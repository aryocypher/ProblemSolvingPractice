# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        
        q=deque()
        levels=0
        q.append(root)
        while len(q)>0:
            levels+=1
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
        return levels   