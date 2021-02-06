#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#
# https://leetcode-cn.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (49.09%)
# Likes:    340
# Dislikes: 0
# Total Accepted:    54.4K
# Total Submissions: 110.7K
# Testcase Example:  '[[1,2]]'
#
# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
# 
# 注意:
# 
# 
# 可以认为区间的终点总是大于它的起点。
# 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
# 
# 
# 示例 1:
# 
# 
# 输入: [ [1,2], [2,3], [3,4], [1,3] ]
# 
# 输出: 1
# 
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
# 
# 
# 示例 2:
# 
# 
# 输入: [ [1,2], [1,2], [1,2] ]
# 
# 输出: 2
# 
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
# 
# 
# 示例 3:
# 
# 
# 输入: [ [1,2], [2,3] ]
# 
# 输出: 0
# 
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
# 
#
#
from typing import List
# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or not intervals[0]:
            return 0
        intervals.sort(key = lambda x: (x[0], x[1]))
        start = intervals[-1][0]
        res = 0
        for i in range(len(intervals)-2, -1, -1):
            if intervals[i][1] > start:
                res += 1
            else:
                start = intervals[i][0]
        return res

# @lc code=end
so = Solution()
ans = so.eraseOverlapIntervals([ [1,2], [2,3] ])
print(ans)
