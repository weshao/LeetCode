#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#
# https://leetcode-cn.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (45.13%)
# Likes:    691
# Dislikes: 0
# Total Accepted:    79.2K
# Total Submissions: 176K
# Testcase Example:  '[1,1,1]\n2'
#
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
# 
# 示例 1 :
# 
# 
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
# 
# 
# 说明 :
# 
# 
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        pre = 0
        count = 0
        for num in nums:
            pre += num
            if (pre - k) in hashmap:
                count += hashmap[pre - k]
            hashmap[pre] = hashmap.get(pre, 0) + 1
        return count
# @lc code=end
so = Solution()
# ans = so.subarraySum([4, 2, 1, -1, 3, 3, 1, 4, -5], 6)
ans = so.subarraySum([-1, -1, 1], 0)
print(ans)
