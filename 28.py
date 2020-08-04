class Solution:
    def strStr(self, haystack, needle):

        n = len(needle)
        for end in range(len(haystack) - n + 1):
            if haystack[end:end+n] == needle:
                return end
        return -1

test = Solution()
ans = test.strStr('a', '')
print(ans)