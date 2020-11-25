#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        leftMax = 0
        rightMax = 0
        waterSum = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < leftMax:
                waterSum += leftMax - height[left]
                left += 1
            elif height[right] < rightMax:
                waterSum += rightMax - height[right]
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return waterSum
            


# @lc code=end
test = Solution()
ans = test.trap([])
print(ans)