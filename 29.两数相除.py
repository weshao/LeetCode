#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = False
        if dividend == 0:
            return 0
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            neg = True
        dividend, divisor = abs(dividend), abs(divisor)
        
        res = 1
        result = 0
        ori_divisor = divisor
        while divisor <= dividend:
            result += res
            dividend -= divisor
            divisor = divisor << 1
            res = res << 1

        while dividend >= ori_divisor:
            divisor = divisor >> 1
            res = res >> 1
            if dividend >= divisor:
                result += res
                dividend -= divisor
        if neg and result > 2 ** 31 or (not neg and result > (2 ** 31 - 1)):
            return 2 ** 31 - 1
        return result if not neg else -result




# @lc code=end
so = Solution()
ans = so.divide(-2147483648, -1)
print(ans)
