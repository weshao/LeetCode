class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        l = ''
        while strs:
            l = []
            s = []
            strs.sort()
            for i in range(len(strs)):
                s.append(list(strs[i]))

            while s[0]:
                f = s[0].pop(0)
                m = 0
                for i in range(1, len(s)):
                    if f == s[i][0]:
                        s[i].pop(0)
                        m += 1
                if m == len(s) - 1:
                    l.append(f)
                else:
                    break
            if l:
                return ''.join(l)
            else:
                return ''
        return ''