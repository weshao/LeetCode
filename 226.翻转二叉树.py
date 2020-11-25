#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#
# https://leetcode-cn.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (77.50%)
# Likes:    686
# Dislikes: 0
# Total Accepted:    160.8K
# Total Submissions: 207.4K
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# 翻转一棵二叉树。
# 
# 示例：
# 
# 输入：
# 
# ⁠    4
# ⁠  /   \
# ⁠ 2     7
# ⁠/ \   / \
# 1   3 6   9
# 
# 输出：
# 
# ⁠    4
# ⁠  /   \
# ⁠ 7     2
# ⁠/ \   / \
# 9   6 3   1
# 
# 备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：
# 
# 谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
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
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        return self.invertTreeRecur(root)
    def invertTreeRecur(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.invertTreeRecur(root.left)
            self.invertTreeRecur(root.right)
        return root
# @lc code=end

tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)
# tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)

so = Solution()
ans = so.invertTree(tree)
print(ans)
