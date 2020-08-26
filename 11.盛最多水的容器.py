#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from typing import List
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxWater = 0
        while left < right:
            maxWater = max(maxWater, (right - left)*min(height[left], height[right]))
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return maxWater
# @lc code=end
test = Solution()
ans = test.maxArea([1,8,6,2,5,4,8,3,7])
print(ans)

