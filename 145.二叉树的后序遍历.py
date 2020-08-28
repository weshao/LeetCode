#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.postorderTraversal_recur(root)
    def postorderTraversal_recur(self, root):
        if root is None:
            return []
        return self.postorderTraversal_recur(root.left) + self.postorderTraversal_recur(root.right) + [root.val]
# @lc code=end

