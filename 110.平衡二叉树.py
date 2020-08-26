#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return True if self.isBalanced_recur(root) is not False else False
    def isBalanced_recur(self, root):
        if root.left is None and root.right is None:
            return 0
        left = 0
        right = 0
        if root.left:
            if self.isBalanced_recur(root.left) is False:
                return False
            left = 1 + self.isBalanced_recur(root.left)
        if root.right:
            if self.isBalanced_recur(root.right) is False:
                return False
            right = 1 + self.isBalanced_recur(root.right)
        if abs(left - right) > 1:
            return False
        else:
            return max(left, right)

# @lc code=end

a = TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)
a.right.right.right = TreeNode(7)
test = Solution()
ans = test.isBalanced(a)
print(ans)
