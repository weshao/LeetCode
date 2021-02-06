#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (45.60%)
# Likes:    602
# Dislikes: 0
# Total Accepted:    233.3K
# Total Submissions: 511.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
# 
# 
# 示例 2：
# 
# 
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 
# 
# 示例 3：
# 
# 
# 输入：digits = [0]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[0] == 0:
            digits[-1] = 1
            return digits
        strD = [str(digits[i]) for i in range(len(digits))]
        num = int(''.join(strD))
        newNum = num + 1
        newStrD = str(newNum)
        newList = [int(numS) for numS in newStrD]
        return newList
# @lc code=end
so = Solution()
ans = so.plusOne([0, 0])
print(ans)