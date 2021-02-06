#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (50.59%)
# Likes:    459
# Dislikes: 0
# Total Accepted:    88.9K
# Total Submissions: 175.2K
# Testcase Example:  '"25525511135"'
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
# 
# 有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
# 
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
# 和 "192.168@1.1" 是 无效的 IP 地址。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
# 
# 
# 示例 2：
# 
# 输入：s = "0000"
# 输出：["0.0.0.0"]
# 
# 
# 示例 3：
# 
# 输入：s = "1111"
# 输出：["1.1.1.1"]
# 
# 
# 示例 4：
# 
# 输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
# 
# 
# 示例 5：
# 
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length <= 3000
# s 仅由数字组成
# 
# 
#
from typing import List
# @lc code=start
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        SEG_COUNT = 4
        ans = list()
        segments = [0] * SEG_COUNT

        def dfs(segId: int, segStart: int):
            if segId == SEG_COUNT:
                if segStart == len(s):
                    ipAddr = '.'.join(str(seg) for seg in segments)
                    ans.append(ipAddr)
                return
            
            if segStart == len(s):
                return
            
            if s[segStart] == '0':
                segments[segId] = 0
                dfs(segId + 1, segStart + 1)

            addr = 0
            for segEnd in range(segStart, len(s)):
                addr = addr * 10 + (ord(s[segEnd]) - ord("0"))
                if 0 < addr <= 0xFF:
                    segments[segId] = addr
                    dfs(segId + 1, segEnd + 1)
                else:
                    break
        
        dfs(0, 0)
        return ans
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        if s == '':
            return result
        self.dfs(s, result, [], 0, 0)
        return result
    def dfs(self, s, result, current, index, i):
        if index == 4:
            if i == len(s):
                result.append('.'.join(current))
            return
        if i >= len(s):
            return

        
        if index == 0 and len(s) - i > 12:
            return
        elif index == 1 and len(s) - i > 9:
            return
        elif index == 2 and len(s) - i > 6:
            return
        elif index == 3 and len(s) - i > 3:
            return

        if s[i] == '0':
            current.append('0')
            self.dfs(s, result, current, index+1, i+1)
            del current[-1]

        else:
            for j in range(i+1, i+4):
                if j <= len(s) and int(s[i:j]) <= 255:
                    current.append(s[i:j])
                    self.dfs(s, result, current, index+1, j)
                    del current[-1]





# @lc code=end
so = Solution()
ans = so.restoreIpAddresses("25525511135")
print(ans)
