#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import List
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
        result = [-1, -1]
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                result[0] = mid
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                result[1] = mid
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = start + 1
        
        return result
# @lc code=end
test = Solution()
ans = test.searchRange([1,3,4,8,8,9,10], 8)
print(ans)