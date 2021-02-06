#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# https://leetcode-cn.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (64.60%)
# Likes:    390
# Dislikes: 0
# Total Accepted:    81K
# Total Submissions: 125.1K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 
# 示例:
# 
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
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

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            n = len(queue)
            for i in range(n):
                tree = queue.popleft()
                if i == n - 1:
                    res.append(tree.val)
                if tree.left:
                    queue.append(tree.left)
                if tree.right:
                    queue.append(tree.right)
        return res

# @lc code=end
tree = TreeNode(1)
tree.left = TreeNode(2)
# tree.left.left = TreeNode(5)
# tree.left.right = TreeNode(3)
# tree.left.right.left = TreeNode(4)
# tree.left.right.left.right = TreeNode(9)
# tree.right = TreeNode(6)
# tree.right.left = TreeNode(7)
# tree.right.left.right = TreeNode(10)
# tree.right.right = TreeNode(8)

so = Solution()
ans = so.rightSideView(tree)
print(ans)

