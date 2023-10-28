# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        res=[]
        if(root==None):
            return res
        q.append(root)
        while(len(q)>0):
            size=len(q)
            levelRes=[]
            for i in range(size):
                data=q.popleft()
                levelRes.append(data.val)
                if data.left!=None:
                    q.append(data.left)
                if data.right!=None:
                    q.append(data.right)
            res.append(levelRes)
                
        return res
        