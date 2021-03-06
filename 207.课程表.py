#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
# https://leetcode-cn.com/problems/course-schedule/description/
#
# algorithms
# Medium (54.83%)
# Likes:    693
# Dislikes: 0
# Total Accepted:    91K
# Total Submissions: 165.9K
# Testcase Example:  '2\n[[1,0]]'
#
# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
# 
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
# 
# 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
# 
# 
# 
# 示例 1:
# 
# 输入: 2, [[1,0]] 
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
# 
# 示例 2:
# 
# 输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
# 
# 
# 
# 提示：
# 
# 
# 输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
# 你可以假定输入的先决条件中没有重复的边。
# 1 <= numCourses <= 10^5
# 
# 
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sortedOrder = []
        if numCourses <= 0:
            return True

        # a. Initialize the graph
        inDegree = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}

        # b. Build the graph
        for edge in prerequisites:
            parent, child = edge[1], edge[0]
            inDegree[child] += 1
            graph[parent].append(child)

        # c. Find all sources
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        # d. For each source add it to sortedOder
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
                    
        if len(sortedOrder) != numCourses:
            return False
        else:
            return True
# @lc code=end

