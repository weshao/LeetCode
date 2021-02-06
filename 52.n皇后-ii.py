#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        count = [0]
        map = set()
        d1 = set()
        d2 = set()
        self.backtracking(map, d1, d2, n, 0, count)
        return count[0]

    def backtracking(self, map, d1, d2, n, index, count):
        if index == n:
            count[0] += 1
            return count
        
        # if index == 0:
        #     for i in range(n):
        #         map.add(i)
        #         d1.add(i)
        #         d2.add(i)
        #         self.backtracking(map, d1, d2, n, index+1, count)
        #         map.remove(i)
        #         d1.remove(i)
        #         d2.remove(i)
        
        # else:
        for i in range(n):
            if i in map or index - i in d1 or index + i in d2:
                continue
            
            map.add(i)
            d1.add(index - i)
            d2.add(index + i)
            self.backtracking(map, d1, d2, n, index+1, count)
            map.remove(i)
            d1.remove(index - i)
            d2.remove(index + i)
        return
# @lc code=end
so = Solution()
ans = so.totalNQueens(5)
print(ans)
