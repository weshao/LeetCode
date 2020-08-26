import math
# from typing import NamedTuple

# class Solution:
#     def minJump(self, jump: List[int]) -> int:
#         dp = [math.inf for _ in range(len(jump))]
#         dp[0] = 1
#         minJump = math.inf
#         for start in range(len(jump)):
#             end = start + jump[start]
#             if end >= len(jump):
#                 minJump = min(minJump, dp[start])
#             else:
#                 dp[end] = min(dp[end], dp[start] + 1)
#                 for left in range(end):
#                     dp[left] = min(dp[left], dp[end] + 1)

#         return minJump



# test = Solution()
# print(test.minJump([2,5,1,1,1,1]))
# print(test.minJump([1]*10000))

# print(test.minJump([2,5,1,1,1,1]))




class Solution:
    def minJump(self, jump) -> int:
        dp = [0 for _ in range(len(jump))]

        def dfs(jump, index):
            n = len(jump)
            if index == n-1:
                return 0
            if dp[index] != 0:
                return dp[index]
            if index == 0 and jump[index] == 0:
                return float('inf')
            totalJ = float('inf')
            start, end = 0, index+jump[index]
            while start < n and start <= end:
                if start == index:
                    start += 1
                    continue
                minJ = dfs(jump, start)
                if minJ != float('inf'):
                    totalJ = min(totalJ, minJ+1)
                start += 1
            dp[index] = totalJ
            return dp[index]
        return dfs(jump, 0)
sol = Solution()
print(sol.minJump([2,5,1,1,1,1]))