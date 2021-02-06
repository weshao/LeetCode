#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (42.02%)
# Likes:    1091
# Dislikes: 0
# Total Accepted:    108.6K
# Total Submissions: 257.4K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
# 
# 
# 
# 
# 
# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
# 
# 
# 
# 
# 
# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
# 
# 
# 
# 示例:
# 
# 输入: [2,1,5,6,2,3]
# 输出: 10
# 
#fcv 


from typing import List
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        n = len(heights)
        left, right = [0] * n, [n] * n
        stack = []
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                right[stack[-1]] = i
                stack.pop()
            stack.append(i)
        
        
        stack = []
        for i in range(n-1, 0, -1):
            while stack and heights[i] < heights[stack[-1]]:
                left[stack[-1]] = i
                stack.pop()
            stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n))
        return ans


# @lc code=end 
so = Solution()
ans = so.largestRectangleArea([2,1,5,6,2,3])
print(ans)
