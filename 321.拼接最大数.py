#
# @lc app=leetcode.cn id=321 lang=python3
#
# [321] 拼接最大数
#
# https://leetcode-cn.com/problems/create-maximum-number/description/
#
# algorithms
# Hard (43.13%)
# Likes:    338
# Dislikes: 0
# Total Accepted:    21.9K
# Total Submissions: 50.9K
# Testcase Example:  '[3,4,6,5]\n[9,1,2,5,8,3]\n5'
#
# 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n)
# 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
# 
# 求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
# 
# 说明: 请尽可能地优化你算法的时间和空间复杂度。
# 
# 示例 1:
# 
# 输入:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# 输出:
# [9, 8, 6, 5, 3]
# 
# 示例 2:
# 
# 输入:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# 输出:
# [6, 7, 6, 0, 4]
# 
# 示例 3:
# 
# 输入:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# 输出:
# [9, 8, 9]
# 
#
from typing import List
# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        maxRes = []
        for i in range(k+1):
            j = k - i
            newNums1 = self.topk(nums1, i)
            newNums2 = self.topk(nums2, j)
            mergeRes = self.merge(newNums1, newNums2)
            if len(mergeRes) > len(maxRes):
                maxRes = mergeRes
            elif len(mergeRes) == len(maxRes):
                maxRes = max(maxRes, mergeRes)
        
        return maxRes


    def merge(self, nums1, nums2):
        i, j = 0, 0
        nums = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i:] > nums2[j:]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i < len(nums1):
            nums += nums1[i:]
        else:
            nums += nums2[j:]
        return nums

    def topk(self, nums, k):
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1] and len(nums) - i > k:
                stack.pop()
                k += 1
            if k > 0:
                stack.append(nums[i])
                k -= 1
        return stack
# @lc code=end
so = Solution()
ans = so.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
print(ans)
