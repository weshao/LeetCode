#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (77.14%)
# Likes:    1007
# Dislikes: 0
# Total Accepted:    220.6K
# Total Submissions: 285.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#
from typing import List
# @lc code=start
""" class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        used = [False for _ in range(size)]
        permutation = []
        self.permute_recur(nums, used, size, 0, [], permutation)
        return permutation
    def permute_recur(self, nums, used, size, depth, current, permutation):
        if depth == size:
            permutation.append(current[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                current.append(nums[i])
                used[i] = True
                self.permute_recur(nums, used, size, depth+1, current, permutation)
                del  current[-1]
                used[i] = False """
                #这一行完了，上一层的permute_recur就完了，然后执行 current[-1]
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if not nums:
            return result
        used = [False for _ in range(len(nums))]

        def dfs(current, index):
            if index == len(nums):
                result.append(list(nums))
                return
            
            for i in range(index, len(nums)):
                # if not used[i]:
                    nums[index], nums[i] = nums[i], nums[index]
                    # current.append(nums[i])
                    # used[i] = True
                    dfs(current, index+1)
                    nums[index], nums[i] = nums[i], nums[index]
                    # del current[-1]
        dfs([], 0)
        return result

# @lc code=end
so = Solution()
ans = so.permute([1, 2, 3])
print(ans)