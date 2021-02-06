#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (51.85%)
# Likes:    292
# Dislikes: 0
# Total Accepted:    90.3K
# Total Submissions: 174.1K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 
# 
# 
# 提示：
# 
# 
# num1 和num2 的长度都小于 5100
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        n1 = len(num1)
        n2 = len(num2)
        res = [0 for _ in range(max(n1, n2))]
        flag = 0
        if n1 > n2:
            for i in range(n1):
                char1 = int(num1[n1-i-1])
                if n2 - i - 1 >= 0:
                    char2 = int(num2[n2-i-1])
                else:
                    char2 = 0
                res[n1-i-1] = str((char1 + char2 + flag) % 10)
                flag = (char1 + char2 + flag) // 10
        else:
            for i in range(n2):
                char2 = int(num2[n2-i-1])
                if n1 - i - 1 >= 0:
                    char1 = int(num1[n1-i-1])
                else:
                    char1 = 0
                res[n2-i-1] = str((char1 + char2 + flag) % 10)
                flag = (char1 + char2 + flag) // 10
                
        
        if flag== 1:
            return '1' + ''.join(res)
        else:
            return ''.join(res)



# @lc code=end
so = Solution()
ans = so.addStrings('0', '0')
print(ans)