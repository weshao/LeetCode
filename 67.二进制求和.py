#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (54.34%)
# Likes:    531
# Dislikes: 0
# Total Accepted:    140.9K
# Total Submissions: 259.1K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 
# 输入为 非空 字符串且只包含数字 1 和 0。
# 
# 
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
# 
# 
# 提示：
# 
# 
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
# 
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na, nb = len(a), len(b)
        i = max(na, nb) - 1
        flag = 0
        c = ['0' for _ in range(max(na, nb))]
        if na > nb:
            b = '0' * (na - nb) + b
        else:
            a = '0' * (nb - na) + a
        while i >= 0 and i >= 0:
            if int(a[i]) + int(b[i]) + flag == 2 :
                c[i] = '0'
                flag = 1
            elif int(a[i]) + int(b[i]) + flag == 3:
                c[i] = '1'
                flag = 1
            else:
                c[i] = str(int(a[i]) + int(b[i]) + flag)
                flag = 0
            i -= 1
        
        if flag == 1:
            return '1' + ''.join(c)
        else:
            return ''.join(c)
        
            

# @lc code=end
so = Solution()
ans = so.addBinary(a = "110010", b = "10111")
print(ans)
