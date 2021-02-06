#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (66.42%)
# Likes:    432
# Dislikes: 0
# Total Accepted:    92.9K
# Total Submissions: 139.8K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 输入:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if not root:
            return res
        def dfs(root, curr):
            if not root.left and not root.right:
                curr.append(str(root.val))
                res.append('->'.join(curr))
                curr.pop()
            
            if root.left:
                curr.append(str(root.val))
                dfs(root.left, curr)
                curr.pop()
            if root.right:
                curr.append(str(root.val))
                dfs(root.right, curr)
                curr.pop()
        dfs(root, [])
        return res
# @lc code=end

