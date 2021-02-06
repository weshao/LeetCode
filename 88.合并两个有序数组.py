#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (49.02%)
# Likes:    725
# Dislikes: 0
# Total Accepted:    248.4K
# Total Submissions: 506.1K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 
# 
# 
# 说明：
# 
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 
# 
# 
# 
# 示例：
# 
# 
# 输入：
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出：[1,2,2,3,5,6]
# 
# 
# 
# 提示：
# 
# 
# -10^9 
# nums1.length == m + n
# nums2.length == n
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2 = 0, 0
        while i1 < m + n and i2 < n:
            if nums2[i2] < nums1[i1]:
                nums1[i1+1: m+n] = nums1[i1:m+n-1]
                nums1[i1] = nums2[i2]
                i2 += 1
            else:
                i1 += 1
        if i2 < n:
            nums1[m+i2:m+n] = nums2[i2:m+n] 
# @lc code=end
        print(nums1)
so = Solution()
ans = so.merge([1,0], 1 , [0,2] ,2)

