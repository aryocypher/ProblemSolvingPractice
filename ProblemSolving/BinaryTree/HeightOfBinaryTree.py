

class Solution:
    # Recursive Method
    def maxDepthRec(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        leftHeight = self.maxDepthRec(root.left)
        rightHeight = self.maxDepthRec(root.right)
        return max(leftHeight, rightHeight)+1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        q = deque()
        levels = 0
        q.append(root)
        while len(q) > 0:
            levels += 1
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
        return levels
