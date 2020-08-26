#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
from typing import List
# @lc code=start
import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        dp = nums
        maxSum = -math.inf
        maxSum = max(maxSum, dp[0])
        for i in range(1, len(nums)):
            if dp[i] <= dp[i] + dp[i - 1]:
                dp[i] = max(dp[i] + dp[i - 1], dp[i])
            maxSum = max(maxSum, dp[i])
        return maxSum

# @lc code=end

test = Solution()
ans = test.maxSubArray([-1, -2])
print(ans)