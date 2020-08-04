# class Solution:
#     def generateParenthesis(self, n):
#         self.result = []
#         self.len = n
#
#         l = ['('] * n
#         r = [')'] * n
#         self.num = n
#         self.ryzen(n, [], l, r )
#
#     def ryzen(self, n, a, l, r):
#         m = n
#         while m:
#             a.append(l.pop())
#             m -= 1
#         a.append(r.pop())
#         if not l:
#             while r:
#                 a.append(r.pop())
#             a = ''.join(a)
#             self.result.append(a)
#             a = []
#             l = ['('] * self.len
#             r = [')'] * self.len
#             if n == 1:
#                 self.ryzen()
#             else:
#                 self.ryzen(n-1,a,l, r)
#         if l:
#             self.ryzen(len(l),a,l,r)

class Solution:
    def generateParenthesis(self, n):
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)
        dfs(cur_str, n, n)
        return res





i = Solution()
a = i.generateParenthesis(3)
