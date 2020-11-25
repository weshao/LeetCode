from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Mirror(self , pRoot ):
        if pRoot is None:
            return pRoot
        tree = deque()
        tree.append(pRoot)
        while tree:
            root = tree.popleft()
            root.left, root.right = root.right, root.left
            if root.left:
                tree.append(root.left)
            if root.right:
                tree.append(root.right)
        
        return pRoot
tree = TreeNode(8)
tree.left = TreeNode(6)
tree.right = TreeNode(10)
tree.right.right = TreeNode(11)

sol = Solution()
ans = sol.Mirror(None)
print(ans)