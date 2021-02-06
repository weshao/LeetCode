#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (61.24%)
# Likes:    401
# Dislikes: 0
# Total Accepted:    109K
# Total Submissions: 177.8K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
# 
# 
# 返回:
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
# 
# 
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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        if not root:
            return result
        def dfs(root, sum, current):
            if not root.left and not root.right:
                if root.val == sum:
                    current.append(root.val)
                    result.append(list(current))
                    del current[-1]
            if root.left:
                current.append(root.val)
                dfs(root.left, sum-root.val, current)
                del current[-1]
            if root.right:
                current.append(root.val)
                dfs(root.right, sum-root.val, current)
                del current[-1]
        dfs(root, sum, [])
        return result

# @lc code=end
tree = TreeNode(5)
tree.left = TreeNode(4)
# tree.left.left = TreeNode(11)
# tree.left.left.left = TreeNode(7)
# tree.left.left.right = TreeNode(2)
# tree.right = TreeNode(8)
# tree.right.left = TreeNode(9)
# tree.right.right = TreeNode(4)
# tree.right.right.left = TreeNode(5)
# tree.right.right.right = TreeNode(1)
so = Solution()
ans = so.pathSum(tree, 9)
print(ans)
