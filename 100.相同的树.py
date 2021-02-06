#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#
# https://leetcode-cn.com/problems/same-tree/description/
#
# algorithms
# Easy (60.19%)
# Likes:    540
# Dislikes: 0
# Total Accepted:    165.2K
# Total Submissions: 274.4K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# 
# 示例 1:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# 输出: true
# 
# 示例 2:
# 
# 输入:      1          1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# 输出: false
# 
# 
# 示例 3:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# 输出: false
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
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        def isSame(p, q):
            if p.val != q.val:
                return False
            if p.left == q.left == p.right == q.right == 0:
                return True

            if (p.left and not q.left) or (p.right and not q.right):
                return False

            if (q.left and not p.left) or (q.right and not p.right):
                return False

            if (p.left and q.left) or (p.right and q.right):
                if p.left and q.left:
                    if not isSame(p.left, q.left):
                        return False
                if p.right and q.right:
                    if not isSame(p.right, q.right):
                        return False
            
                
            return True
        return isSame(p, q)
# @lc code=end
p = TreeNode(1)
p.right = TreeNode(2)

q = TreeNode(1)
q.right = TreeNode(2)

so = Solution()
ans = so.isSameTree(None, None)
print(ans)
