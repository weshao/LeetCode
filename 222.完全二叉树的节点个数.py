#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#
# https://leetcode-cn.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (76.68%)
# Likes:    424
# Dislikes: 0
# Total Accepted:    76.1K
# Total Submissions: 99.2K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
# 
# 完全二叉树
# 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h
# 层，则该层包含 1~ 2^h 个节点。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3,4,5,6]
# 输出：6
# 
# 
# 示例 2：
# 
# 
# 输入：root = []
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目范围是[0, 5 * 10^4]
# 0 
# 题目数据保证输入的树是 完全二叉树
# 
# 
# 
# 
# 进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？
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
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(root, index, depth):
            if not root.left and not root.right:
                if index == depth - 1:
                    return 1
            child = 0
            if index < depth:
                if not root.left:
                    return child
                else:
                    child += dfs(root.left, index+1, depth)
                if not root.right:
                    return child
                else:
                    child += dfs(root.right, index+1, depth)
            return child
        depth = 0
        depthroot = root
        while depthroot:
            depth += 1
            depthroot = depthroot.left
        child = dfs(root, 0, depth)
        res = 2 ** (depth-1) - 1 + child
        return res

                
                
# @lc code=end
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right = TreeNode(3)
tree.right.left = TreeNode(6)
# tree.right.right = TreeNode(7)
so = Solution()
ans = so.countNodes(tree)
print(ans)