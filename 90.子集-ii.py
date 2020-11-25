#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (61.39%)
# Likes:    347
# Dislikes: 0
# Total Accepted:    57K
# Total Submissions: 92.7K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#
from typing import List
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        used = [False for _ in range(len(nums))]
        self.subset_recur(0, nums, used, 0, [], subsets)
        return subsets

    def subset_recur(self, p, nums, used, depth, current, subsets):
        subsets.append(current[:])

        if depth == len(nums):
            return
        
        for i in range(p, len(nums)):
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                # print("here")
                continue
            if not used[i]:
                current.append(nums[i])
                used[i] = True
                self.subset_recur(i, nums, used, depth+1, current, subsets)
                used[i] = False
                del current[-1]
            
# @lc code=end
so = Solution()
ans = so.subsetsWithDup([1, 2, 2])
print(ans)
