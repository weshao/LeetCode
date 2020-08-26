#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        dp0, dp1, temp = 1, 1, 0
        for i in range(2, n+1):
            temp = dp0 + dp1
            dp0, dp1= dp1, temp
            
        return temp
# @lc code=end
test = Solution()
ans = test.climbStairs(3)
print(ans)
