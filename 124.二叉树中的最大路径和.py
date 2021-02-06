#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (43.23%)
# Likes:    835
# Dislikes: 0
# Total Accepted:    90.5K
# Total Submissions: 209.2K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空二叉树，返回其最大路径和。
# 
# 本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# 输出：6
# 
# 
# 示例 2：
# 
# 输入：[-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# 输出：42
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
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = [-float('inf')]
        def dfs(root):
            if not root.left and not root.right:
                max_sum[0] = max(max_sum[0], root.val)
                return root.val
            
            left = 0
            right = 0
            _sum = 0
            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)
            _sum1 = root.val + left + right
            _sum2 = root.val + left
            _sum3 = root.val + right
            
            max_sum[0] = max(max_sum[0], _sum1, _sum2, _sum3, root.val)
            return max(_sum2, _sum3, root.val)
        dfs(root)
        return max_sum[0]
# @lc code=end
node = TreeNode(-10)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)

# node = TreeNode(-1)
# node.left = TreeNode(-2)
# node.right = TreeNode(6)

so = Solution()
ans = so.maxPathSum(node)
print(ans)
