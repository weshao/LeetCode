#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (62.18%)
# Likes:    532
# Dislikes: 0
# Total Accepted:    121.7K
# Total Submissions: 195.5K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10 
# 
# 
#
from typing import List
# @lc code=start
""" class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        used = [False for _ in range(size)]
        nums.sort()
        permutation = []
        self.permute_recur(nums, used, size, 0, [], permutation)
        return permutation
    def permute_recur(self, nums, used, size, depth, current, permutation):
        if depth == size:
            permutation.append(current[:])
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                # print(i)
                continue
            if not used[i]:
                current.append(nums[i])
                used[i] = True
                self.permute_recur(nums, used, size, depth+1, current, permutation)
                del  current[-1]
                used[i] = False
                #这一行完了，上一层的permute_recur就完了，然后执行 current[-1]

 """
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        if not nums:
            return result
        used = [False for _ in range(len(nums))]

        def dfs(current, index):
            if index == len(nums):
                result.append(list(current))
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                if not used[i]:
                    current.append(nums[i])
                    used[i] = True
                    dfs(current, index+1)
                    used[i] = False
                    del current[-1]
        nums.sort()
        dfs([], 0)
        return result


# # @lc code=end
so = Solution()
ans = so.permuteUnique([0,1,0,0,9])
print(ans)

