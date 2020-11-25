#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#
# https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (71.98%)
# Likes:    141
# Dislikes: 0
# Total Accepted:    44.6K
# Total Submissions: 62K
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证
# ，新值和原始二叉搜索树中的任意节点值都不同。
# 
# 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [4,2,7,1,3], val = 5
# 输出：[4,2,7,1,3,5]
# 解释：另一个满足题目要求可以通过的树是：
# 
# 
# 
# 示例 2：
# 
# 
# 输入：root = [40,20,60,10,30,50,70], val = 25
# 输出：[40,20,60,10,30,50,70,null,null,25]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# 输出：[4,2,7,1,3,5]
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 给定的树上的节点数介于 0 和 10^4 之间
# 每个节点都有一个唯一整数值，取值范围从 0 到 10^8
# -10^8 
# 新值和原始二叉搜索树中的任意节点值都不同
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
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.dfs(root, val)
    
    def dfs(self, root, val):
        if not root:
            return TreeNode(val)

        if root.val < val:
            root.right = self.dfs(root.right, val)
        
        if root.val > val:
            root.left = self.dfs(root.left, val)
        
        return root
        

        
# @lc code=end
tree = TreeNode(4)
tree.left = TreeNode(2)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right = TreeNode(7)

so = Solution()
ans = so.insertIntoBST(tree, 5)
print(ans)