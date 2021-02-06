#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
# https://leetcode-cn.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (51.99%)
# Likes:    586
# Dislikes: 0
# Total Accepted:    87.4K
# Total Submissions: 167.9K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
# 
# 
# 
# 示例 :
# 给定二叉树
# 
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
# 
# 
# 
# 注意：两结点之间的路径长度是以它们之间边的数目表示。
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = [0]
        def dfs(root):
            if root.left is None and root.right is None:
                return 0
            left = 0
            right = 0
            if root.left:
                left = 1 + dfs(root.left)
            if root.right:
                right = 1 + dfs(root.right)
            res[0] = max(res[0], left + right)

            return max(left, right)
        dfs(root)
        return res[0]

            
            

        
# @lc code=end
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.left.left.left = TreeNode(6)
tree.left.left.left.left = TreeNode(7)
tree.left.right.right = TreeNode(5)
tree.left.right.right.left = TreeNode(5)
tree.right = TreeNode(3)
so = Solution()
ans = so.diameterOfBinaryTree(tree)
print(ans)