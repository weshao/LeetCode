#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#
# https://leetcode-cn.com/problems/24-game/description/
#
# algorithms
# Hard (54.51%)
# Likes:    263
# Dislikes: 0
# Total Accepted:    21.4K
# Total Submissions: 39.4K
# Testcase Example:  '[4,1,8,7]'
#
# 你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。
# 
# 示例 1:
# 
# 输入: [4, 1, 8, 7]
# 输出: True
# 解释: (8-4) * (7-1) = 24
# 
# 
# 示例 2:
# 
# 输入: [1, 2, 1, 2]
# 输出: False
# 
# 
# 注意:
# 
# 
# 除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
# 每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1
# 是不允许的。
# 你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        TARGET = 24
        EPSILON = 1e-6
        ADD, MULTIPLY, SUBSTRACT, DIVIDE = 0, 1, 2, 3

        def solve(nums):
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPSILON
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = list()
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                        for k in range(4):
                            if k < 2 and i > j:
                                continue
                            if k == ADD:
                                newNums.append(x + y)
                            elif k == MULTIPLY:
                                newNums.append(x * y)
                            elif k == SUBSTRACT:
                                newNums.append(x - y)
                            elif k == DIVIDE:
                                if abs(y) < EPSILON:
                                    continue
                                newNums.append(x / y)
                            if solve(newNums):
                                return True
                            newNums.pop()
            return False
        return solve(nums)
# @lc code=end
so = Solution()
ans = so.judgePoint24([3, 4, 6, 7])
print(ans)
