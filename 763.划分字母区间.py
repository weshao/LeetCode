#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
# https://leetcode-cn.com/problems/partition-labels/description/
#
# algorithms
# Medium (76.59%)
# Likes:    430
# Dislikes: 0
# Total Accepted:    55.4K
# Total Submissions: 72.4K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。
# 
# 
# 
# 示例：
# 
# 
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
# 
# 
# 
# 
# 提示：
# 
# 
# S的长度在[1, 500]之间。
# S只包含小写字母 'a' 到 'z' 。
# 
# 
#
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return 0
        intervals = {}
        for i in range(len(S)):
            if S[i] not in intervals:
                intervals[S[i]] = [i, i]
            else:
                intervals[S[i]][1] = i
        ni = list(intervals.values())
        res = []
        ni.sort(key=lambda x:x[0])
        start, end = ni[0][0], ni[0][1]
        for i in range(1, len(ni)):
            if ni[i][0] > end:
                res.append(end - start + 1)
                start = ni[i][0]
                end = ni[i][1]
            else:
                end = max(end, ni[i][1])
        res.append(end - start + 1)
        return res 
            

# @lc code=end
so = Solution()
ans = so.partitionLabels(S = "")
print(ans)
