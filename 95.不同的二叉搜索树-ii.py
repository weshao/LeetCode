#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (66.82%)
# Likes:    738
# Dislikes: 0
# Total Accepted:    69.3K
# Total Submissions: 103.7K
# Testcase Example:  '3'
#
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
# 
# 
# 
# 示例：
# 
# 输入：3
# 输出：
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 8
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []

        def dfs(start, end):
            if start > end:
                return [None,]

            AllNodes = []

            for i in range(start, end+1):
                leftNodes = dfs(start, i-1)
                rightNodes = dfs(i+1, end)

                for leftNode in leftNodes:
                    for rightNode in rightNodes:
                        l = TreeNode(i)
                        l.left = leftNode
                        l.right = rightNode
                        AllNodes.append(l)
            
            return AllNodes
        
        return dfs(1, n)
        
            
# @lc code=end
so = Solution()
ans = so.generateTrees(3)
print(ans)