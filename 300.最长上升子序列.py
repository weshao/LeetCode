#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for _ in range(n+1)] for _ in range(n)]
        return find_LIS_length_recursive(dp, nums, 0, -1)


def find_LIS_length_recursive(dp, nums, currentIndex, previousIndex):
  if currentIndex == len(nums):
    return 0

  if dp[currentIndex][previousIndex + 1] == -1:
    # include nums[currentIndex] if it is larger than the last included number
    c1 = 0
    if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
      c1 = 1 + find_LIS_length_recursive(dp, nums, currentIndex + 1, currentIndex)

    c2 = find_LIS_length_recursive(
      dp, nums, currentIndex + 1, previousIndex)
    dp[currentIndex][previousIndex + 1] = max(c1, c2)

  return dp[currentIndex][previousIndex + 1]
        
# @lc code=end

