#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
from typing import List
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        susbsets = []
        susbsets.append([])
        for num in nums:
            n = len(susbsets)
            for i in range(n):
                susbset = susbsets[i]
                set = list(susbset)
                set.append(num)
                susbsets.append(set)
        return susbsets
# @lc code=end
test = Solution()
ans = test.subsets([1, 2, 3, 4])
print(ans)

