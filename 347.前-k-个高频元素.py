#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
# https://leetcode-cn.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (61.77%)
# Likes:    611
# Dislikes: 0
# Total Accepted:    126.1K
# Total Submissions: 203.9K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
# 
# 
# 
# 示例 1:
# 
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 
# 
# 示例 2:
# 
# 输入: nums = [1], k = 1
# 输出: [1]
# 
# 
# 
# 提示：
# 
# 
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
# 你可以按任意顺序返回答案。
# 
# 
#
from collections import Counter
from typing import List
# @lc code=start
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        if not nums or not k:
            return res
        num_count = Counter(nums)
        maxHeap = []
        for key, value in num_count.items():
            heappush(maxHeap, (-value, key))
        while k:
            res.append(heappop(maxHeap)[1])
            k -= 1
        return res

# @lc code=end
so = Solution()
ans = so.topKFrequent(nums = [], k = 1)
print(ans)
