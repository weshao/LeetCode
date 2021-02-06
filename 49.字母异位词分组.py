#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (64.09%)
# Likes:    606
# Dislikes: 0
# Total Accepted:    152.1K
# Total Submissions: 233.2K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 
# 示例:
# 
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# 说明：
# 
# 
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
# 
# 
#
from typing import List
# @lc code=start
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashtable = defaultdict(list)
        if not strs:
            return result
        for _str in strs:
            flag = False
            dic = ''.join(sorted(_str))
            hashtable[dic].append(_str)
        
        return list(hashtable.values())
# @lc code=end
so = Solution()
ans = so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat", "eaat", "aaet", "eeat"])
print(ans)