#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
from typing import List
# @lc code=start
from heapq import *
import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        minHeap = []
        maxHeap = []
        
        for num in nums1:
            if not maxHeap or -maxHeap[0] >= num:
                heappush(maxHeap, -num)
            else:
                heappush(minHeap, num)
            if len(maxHeap) > len(minHeap) + 1:
                heappush(minHeap, - heappop(maxHeap))
            elif len(maxHeap) < len(minHeap):
                heappush(maxHeap, - heappop(minHeap))
        
        for num in nums2:
            if not maxHeap or -maxHeap[0] >= num:
                heappush(maxHeap, -num)
            else:
                heappush(minHeap, num)
            if len(maxHeap) > len(minHeap) + 1:
                heappush(minHeap, - heappop(maxHeap))
            elif len(maxHeap) < len(minHeap):
                heappush(maxHeap, - heappop(minHeap))
        
        if len(maxHeap) == len(minHeap):
            return (-maxHeap[0] + minHeap[0]) / 2
        else:
            return -maxHeap[0]
             
# @lc code=end
test = Solution()
print(test.findMedianSortedArrays([1, 3], [2]))
print("finish")