#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
#
# https://leetcode-cn.com/problems/binary-tree-cameras/description/
#
# algorithms
# Hard (48.83%)
# Likes:    260
# Dislikes: 0
# Total Accepted:    19K
# Total Submissions: 39K
# Testcase Example:  '[0,0,null,0,0]'
#
# 给定一个二叉树，我们在树的节点上安装摄像头。
# 
# 节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
# 
# 计算监控树的所有节点所需的最小摄像头数量。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[0,0,null,0,0]
# 输出：1
# 解释：如图所示，一台摄像头足以监控所有节点。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：[0,0,null,0,null,0,null,null,0]
# 输出：2
# 解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
# 
# 
# 
# 提示：
# 
# 
# 给定树的节点数的范围是 [1, 1000]。
# 每个节点的值都是 0。
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
""" class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return [float('inf'), 0, 0]
            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)
            a = lc + rc + 1
            b = min(a, la + rb, ra + lb)
            c = min(a, lb + rb)
            return [a, b, c]
        a, b, c = dfs(root)
        return b
        

so = Solution()
ans = so.minCameraCover(None)
print(ans)

 """
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return [float('inf'), 0, 0]
            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)
            
            a = lc + rc + 1
            b = min(a, la + rb, lb + ra)
            c = min(a, lb + rb)

            return [a, b, c]
        _, b, _ =  dfs(root)
        return b
# @lc code=end