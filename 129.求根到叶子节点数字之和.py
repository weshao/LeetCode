#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#
# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (66.29%)
# Likes:    297
# Dislikes: 0
# Total Accepted:    79.1K
# Total Submissions: 119.1K
# Testcase Example:  '[1,2,3]'
#
# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
# 
# 例如，从根到叶子节点路径 1->2->3 代表数字 123。
# 
# 计算从根到叶子节点生成的所有数字之和。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.
# 
# 示例 2:
# 
# 输入: [4,9,0,5,1]
# ⁠   4
# ⁠  / \
# ⁠ 9   0
# / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026.
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(root,cur):
            res = 0

            if not root.left and not root.right:
                res = cur * 10 + root.val
                cur = (cur - root.val) / 10
                return res 
            
            if root.left:
                cur = cur * 10 + root.val
                res += dfs(root.left,cur)
                cur = (cur - root.val) / 10
            
            if root.right:
                cur = cur * 10 + root.val
                res += dfs(root.right, cur)
                cur = (cur - root.val) / 10
            
            return int(res)
        return dfs(root, 0)
# @lc code=end
tree = TreeNode(4)
tree.left = TreeNode(9)
tree.left.left = TreeNode(5)
tree.left.right = TreeNode(1)
tree.right = TreeNode(0)
so = Solution()
ans = so.sumNumbers(tree)
print(ans)
