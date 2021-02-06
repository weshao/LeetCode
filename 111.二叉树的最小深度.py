#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (45.67%)
# Likes:    425
# Dislikes: 0
# Total Accepted:    169.3K
# Total Submissions: 367.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
# 
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 
# 说明：叶子节点是指没有子节点的节点。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数的范围在 [0, 10^5] 内
# -1000 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        tree = deque([root])
        depth = 1
        while tree:
            for _ in range(len(tree)):
                node = tree.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
            depth += 1
        return depth      

# @lc code=end
node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)

so = Solution()
ans = so.minDepth(node)
print(ans)

