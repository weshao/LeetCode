#
# @lc app=leetcode.cn id=488 lang=python3
#
# [488] 祖玛游戏
#
# https://leetcode-cn.com/problems/zuma-game/description/
#
# algorithms
# Hard (41.58%)
# Likes:    67
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 6K
# Testcase Example:  '"WRRBBW"\n"RB"'
#
# 回忆一下祖玛游戏。现在桌上有一串球，颜色有红色(R)，黄色(Y)，蓝色(B)，绿色(G)，还有白色(W)。 现在你手里也有几个球。
# 
# 
# 每一次，你可以从手里的球选一个，然后把这个球插入到一串球中的某个位置上（包括最左端，最右端）。接着，如果有出现三个或者三个以上颜色相同的球相连的话，就把它们移除掉。重复这一步骤直到桌上所有的球都被移除。
# 
# 找到插入并可以移除掉桌上所有球所需的最少的球数。如果不能移除桌上所有的球，输出 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：board = "WRRBBW", hand = "RB"
# 输出：-1
# 解释：WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW
# 
# 
# 示例 2：
# 
# 
# 输入：board = "WWRRBBWW", hand = "WRBRW"
# 输出：2
# 解释：WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty
# 
# 
# 示例 3：
# 
# 
# 输入：board = "G", hand = "GGGGG"
# 输出：2
# 解释：G -> G[G] -> GG[G] -> empty 
# 
# 
# 示例 4：
# 
# 
# 输入：board = "RBYYBBRRB", hand = "YRBGB"
# 输出：3
# 解释：RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] ->
# empty 
# 
# 
# 
# 
# 提示：
# 
# 
# 你可以假设桌上一开始的球中，不会有三个及三个以上颜色相同且连着的球。
# 1 
# 1 
# 输入的两个字符串均为非空字符串，且只包含字符 'R','Y','B','G','W'。
# 
# 
#

# @lc code=start
import collections
from typing import Counter


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def backtrack(borad):
            if not borad: return 0
            i = 0
            ans = 6
            while i < len(borad):
                j = i + 1
                while j < len(borad) and borad[i] == borad[j]: j+= 1
                balls = 3 - (j - i)
                if counter[borad[i]] >= balls:
                    balls = max(0, balls)
                    counter[borad[i]] -= balls
                    ans = min(ans, balls + backtrack(borad[:i] + borad[j:]))
                    counter[borad[i]] += balls
                i = j
            return ans

        counter = collections.Counter(hand)
        ans = backtrack(board)
        return -1 if ans > 5 else ans
# @lc code=end
so = Solution()
ans = so.findMinStep("WWBBWBBWW", "BB")
print(ans)
