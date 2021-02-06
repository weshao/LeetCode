#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
# https://leetcode-cn.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (53.42%)
# Likes:    353
# Dislikes: 0
# Total Accepted:    224.5K
# Total Submissions: 408K
# Testcase Example:  '[1,2,3,1]'
#
# 给定一个整数数组，判断是否存在重复元素。
# 
# 如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: [1,2,3,1]
# 输出: true
# 
# 示例 2:
# 
# 
# 输入: [1,2,3,4]
# 输出: false
# 
# 示例 3:
# 
# 
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true
# 
#
from typing import List

# @lc code=start
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for num in count.values():
            if num > 1:
                return True
        return False
# @lc code=end
so = Solution()
ans = so.containsDuplicate([1,1])
print(ans)