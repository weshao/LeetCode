#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
from typing import List
# @lc code=start
from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for i in range(len(nums)):
            heappush(maxHeap, - nums[i])
        for _ in range(k):
            result = heappop(maxHeap)
        return -result
# @lc code=end

test = Solution()
ans = test.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print(ans)