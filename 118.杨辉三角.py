#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (67.78%)
# Likes:    375
# Dislikes: 0
# Total Accepted:    116.5K
# Total Submissions: 171.7K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
#
from typing import List
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result
        result.append([1])
        while numRows > 1:
            pre = result[-1]
            new = [1]
            for i in range(len(pre)-1):
                new.append(pre[i] + pre[i + 1])
            new.append(1)
            result.append(new)
            numRows -= 1
        return result

            

# @lc code=end
so = Solution()
ans = so.generate(2)
print(ans)
