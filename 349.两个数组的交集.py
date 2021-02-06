#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (73.31%)
# Likes:    310
# Dislikes: 0
# Total Accepted:    151.1K
# Total Submissions: 205.7K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
# 
# 
# 示例 2：
# 
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
# 
# 
# 
# 说明：
# 
# 
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。
# 
# 
#
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if not nums1 or not nums2:
            return res
        h1 = Counter(nums1)
        h2 = Counter(nums2)
        for key in h2.keys():
            if key in h1:
                res.append(key)
        return res
# @lc code=end
so = Solution()
ans = so.intersection(nums1 = [], nums2 = [])
print(ans)
