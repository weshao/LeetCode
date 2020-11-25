#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        multiSum = 0
        flag = 0
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                multiSum += int(num1[i]) * int(num2[j]) * 10**((n1-1-i)+(n2-1-j))
        return str(multiSum)


         
# @lc code=end
test = Solution()
ans = test.multiply('0', '0')
print(ans)
