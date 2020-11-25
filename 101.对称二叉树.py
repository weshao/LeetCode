#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (53.13%)
# Likes:    1119
# Dislikes: 0
# Total Accepted:    229.8K
# Total Submissions: 432.4K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# 进阶：
# 
# 你可以运用递归和迭代两种方法解决这个问题吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         return self.isSymmetricRecur(root.left, root.right)
#     def isSymmetricRecur(self, root1, root2):
#         if root1 is None and root2 is None:
#             return True
#         if not (root1 and root2):
#             return False
#         if root1.val != root2.val:
#             return False
#         return self.isSymmetricRecur(root1.left, root2.right) and self.isSymmetricRecur(root1.right, root2.left)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or not(root.left or root.right):
            return True
        queue = [root.left, root.right]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not(left or right):
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            queue.append(left.right)
            queue.append(right.left)

            queue.append(right.right)
            queue.append(left.left)
        return True

        


        
# @lc code=end
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.right = TreeNode(3)
tree.right.right = TreeNode(3)
so = Solution()
ans = so.isSymmetric(tree)
print(ans)
