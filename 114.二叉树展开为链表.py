#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (71.54%)
# Likes:    676
# Dislikes: 0
# Total Accepted:    102.1K
# Total Submissions: 142.5K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给定一个二叉树，原地将它展开为一个单链表。
# 
# 
# 
# 例如，给定二叉树
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 将其展开为：
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root.left and not root.right:
                return root
            right = None
            if root.right:
                right = root.right
            if root.left:
                root.right = dfs(root.left)
            else:
                root.right = None
            root.left = None
            newright = root
            while newright.right:
                newright = newright.right
            if right:
                newright.right = dfs(right)
            
            return root

        if root:
            dfs(root)
        # return root
# @lc code=end
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right = TreeNode(5)
# tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)
so = Solution()
ans = so.flatten(tree)
print(ans)
