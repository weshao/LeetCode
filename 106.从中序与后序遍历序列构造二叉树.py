#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (70.82%)
# Likes:    426
# Dislikes: 0
# Total Accepted:    83K
# Total Submissions: 117.1K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 根据一棵树的中序遍历与后序遍历构造二叉树。
# 
# 注意:
# 你可以假设树中没有重复的元素。
# 
# 例如，给出
# 
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 
# 返回如下的二叉树：
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
#
from typing import List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        def dfs(postorder, inorder):
            if postorder == [] or inorder == []:
                return None
            tree = TreeNode(postorder[-1])
            location = inorder.index(postorder[-1])
            tree.left = dfs(postorder[:location], inorder[:location])
            tree.right = dfs(postorder[location:-1], inorder[location+1:])

            return tree
        return dfs(postorder, inorder)
# @lc code=end
so = Solution()
ans = so.buildTree([9,3,15,20,7], [9,15,7,20,3])
print(ans)

