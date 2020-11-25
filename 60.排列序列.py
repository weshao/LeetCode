#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#
# https://leetcode-cn.com/problems/permutation-sequence/description/
#
# algorithms
# Hard (51.59%)
# Likes:    439
# Dislikes: 0
# Total Accepted:    67.9K
# Total Submissions: 131.4K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
# 
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# 给定 n 和 k，返回第 k 个排列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3, k = 3
# 输出："213"
# 
# 
# 示例 2：
# 
# 
# 输入：n = 4, k = 9
# 输出："2314"
# 
# 
# 示例 3：
# 
# 
# 输入：n = 3, k = 1
# 输出："123"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#

# @lc code=start
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        used = [str(i + 1) for i in range(n)]
        result = ''
        while n:
            first = (k - 1)// math.factorial(n-1)
            result += used[first]
            del used[first]
            k = k % math.factorial(n-1)
            n -= 1
        # result += ''.join(used)
        return result
# @lc code=end
so = Solution()
ans = so.getPermutation(4, 9)
print(ans)
