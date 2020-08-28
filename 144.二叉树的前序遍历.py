#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
from typing import List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self.preorderTraversal_recur(root)

    def preorderTraversal_recur(self, root):
        if root is None:
            return []
        return [root.val] + self.preorderTraversal_recur(root.left) + self.preorderTraversal(root.right)

# @lc code=end
tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)
test = Solution()
ans = test.preorderTraversal(tree)
print(ans)

