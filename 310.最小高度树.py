#
# @lc app=leetcode.cn id=310 lang=python3
#
# [310] 最小高度树
#
# https://leetcode-cn.com/problems/minimum-height-trees/description/
#
# algorithms
# Medium (36.38%)
# Likes:    280
# Dislikes: 0
# Total Accepted:    14.2K
# Total Submissions: 39K
# Testcase Example:  '4\n[[1,0],[1,2],[1,3]]'
#
# 树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
# 
# 给你一棵包含 n 个节点的数，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中
# edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。
# 
# 可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为
# 最小高度树 。
# 
# 请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。
# 树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 4, edges = [[1,0],[1,2],[1,3]]
# 输出：[1]
# 解释：如图所示，当根是标签为 1 的节点时，树的高度是 1 ，这是唯一的最小高度树。
# 
# 示例 2：
# 
# 
# 输入：n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# 输出：[3,4]
# 
# 
# 示例 3：
# 
# 
# 输入：n = 1, edges = []
# 输出：[0]
# 
# 
# 示例 4：
# 
# 
# 输入：n = 2, edges = [[0,1]]
# 输出：[0,1]
# 
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# edges.length == n - 1
# 0 i, bi < n
# ai != bi
# 所有 (ai, bi) 互不相同
# 给定的输入 保证 是一棵树，并且 不会有重复的边
# 
# 
#
from typing import List
# @lc code=start
from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        inDegree = defaultdict(int)

        for edge1, edge2 in edges:
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)
            inDegree[edge1] += 1
            inDegree[edge2] += 1
        
        leaves = deque([])
        for i in range(n):
            if inDegree[i] == 1:
                leaves.append(i)
        
        numLeaves = n
        while numLeaves > 2:
            l = len(leaves)
            numLeaves -= l
            for _ in range(l):
                leave = leaves.popleft()
                for child in graph[leave]:
                    inDegree[child] -= 1
                    if inDegree[child] == 1:
                        leaves.append(child)
        return list(leaves)

# @lc code=end
so = Solution()
ans = so.findMinHeightTrees(n = 2, edges = [[0,1]])
print(ans)
