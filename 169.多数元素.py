#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (65.12%)
# Likes:    834
# Dislikes: 0
# Total Accepted:    250.9K
# Total Submissions: 384.1K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[3,2,3]
# 输出：3
# 
# 示例 2：
# 
# 
# 输入：[2,2,1,1,1,2,2]
# 输出：2
# 
# 
# 
# 
# 进阶：
# 
# 
# 尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
# 
# 
#
from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        # if len(nums) == 1:
        #     return nums[0]
        nums.sort()
        return nums[len(nums)// 2 ]
        


# @lc code=end
so = Solution()
ans = so.majorityElement([2,2,1,3,1,1,4,1,1,5,1,1,6])
print(ans)
