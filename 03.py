class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        while s:
            count = []
            c = []
            for i in range(len(s)):
                if s[i] not in c:
                    c.append(s[i])
                else:
                    count.append(len(c))
                    d = c.index(s[i])
                    c = c[d+1:]
                    c.append(s[i])
            count.append(len(c))
            return max(count)
        return 0

A = Solution()
# B = A.lengthOfLongestSubstring("dvdf")
# C = A.lengthOfLongestSubstring("abcabcbb")
# D = A.lengthOfLongestSubstring("bbbb")
# E = A.lengthOfLongestSubstring("pwwkew")
F = A.lengthOfLongestSubstring("asjrgapa")
print(F)
