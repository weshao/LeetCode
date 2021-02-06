#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
from typing import List
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = False
        for i in range(len(nums)-1, 0, -1): 
            if nums[i] > nums[i-1]:
                rest = nums[i:]
                rest.sort()
                nums[i:] = rest
                j = i
                while j < len(nums)-1 and nums[i-1]>=nums[j]:
                    j += 1
                nums[i-1], nums[j] = nums[j], nums[i-1]
                flag = True
                break

        if not flag:
            nums.reverse()          

# @lc code=end
so = Solution()
ans = so.nextPermutation([1, 3, 2])
print(ans)
