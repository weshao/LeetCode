#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (44.50%)
# Likes:    491
# Dislikes: 0
# Total Accepted:    97K
# Total Submissions: 218K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续
# 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
# 
# 
# 
# 示例：
# 
# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 
# 
# 
# 
# 进阶：
# 
# 
# 如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
# 
# 
#
from typing import List
import bisect
# @lc code=start
class Solution:
    '''
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start, end = 0, 1
        length = len(nums)
        minLen = math.inf
        while end <= length:
            while sum(nums[start:end]) < s and end <= length:
                end += 1
            minLen = min(minLen, end - start)
            start += 1
        
        return minLen if minLen <= length else 0
    '''

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])
        
        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))
        
        return 0 if ans == n + 1 else ans


            
# @lc code=end
sol = Solution()
ans = sol.minSubArrayLen(7, [ 2,3,1,2,4,3])
print(ans)