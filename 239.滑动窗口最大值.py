#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode-cn.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (49.03%)
# Likes:    788
# Dislikes: 0
# Total Accepted:    116.4K
# Total Submissions: 234.8K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
# 
# 返回滑动窗口中的最大值。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1], k = 1
# 输出：[1]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1,-1], k = 1
# 输出：[1,-1]
# 
# 
# 示例 4：
# 
# 
# 输入：nums = [9,11], k = 2
# 输出：[11]
# 
# 
# 示例 5：
# 
# 
# 输入：nums = [4,-2], k = 2
# 输出：[4]
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10^4 
# 1 
# 
# 
#
from typing import List
# @lc code=start
from heapq import *
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        if not nums or not k:
            return res
        start = 0
        max_nums = []
        for end in range(len(nums)):
            if end - start >= k:
                num, lo = max_nums[0]
                if nums[start] == - num:
                    while len(max_nums) >= k:
                        num, lo = max_nums[0]
                        if lo <= start:
                            heappop(max_nums)
                        if lo > start:
                            break
                heappush(max_nums, (-nums[end], end))
                num, _ = max_nums[0]
                res.append(-num)
                start += 1
                
            else:
                heappush(max_nums, (-nums[end], end))
                if end == k-1:
                    num, _ = max_nums[0]
                    res.append(-num)

        return res

# @lc code=end
so = Solution()
ans = so.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6],
5)
print(ans)
