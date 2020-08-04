class Solution:
    def test(self,x):
        if x > 1:
            return 0
        x = x + 1
        return x

A = Solution()
b = A.test(2)
print(b)