#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (71.60%)
# Likes:    1059
# Dislikes: 0
# Total Accepted:    181.8K
# Total Submissions: 253.8K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的数字可以无限制重复被选取。
# 
# 说明：
# 
# 
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1：
# 
# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# 示例 2：
# 
# 输入：candidates = [2,3,5], target = 8,
# 所求解集为：
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
# 
# 提示：
# 
# 
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# candidate 中的每个元素都是独一无二的。
# 1 <= target <= 500
# 
# 
#
from typing import List
# @lc code=start
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         allCombination = []
#         candidates.sort()
#         self.allCombinationSum(candidates, target, [], allCombination)
#         return allCombination
    
#     def allCombinationSum(self, candidates, target, currentSum, allCombination):
#         if target == 0:
#             allCombination.append(list(currentSum))
#             return True
#         elif target <0:
#             return
#         for i in range(len(candidates)):
#             currentSum.append(candidates[i])
#             if self.allCombinationSum(candidates[i:], target - candidates[i], currentSum, allCombination):
#                 del currentSum[-1]
#                 break    
#             del currentSum[-1]

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        if not candidates:
            return result
        
        candidates.sort()
        

        def dfs(current, i, target):
            if target == 0:
                result.append(list(current))
                return
            if target < 0:
                return
            
    
            for j in range(i, len(candidates)):
                if candidates[j] <= target:
                    current.append(candidates[j])
                    dfs(current, j, target - candidates[j])
                    del current[-1]
                else:
                    break
            

        # for i in range(len(candidates)):
        #     if candidates[i] <= target:
        dfs([], 0 , target)
        return result
        
# @lc code=end

so = Solution()
ans = so.combinationSum([2,3,5] , 8)
print(ans)