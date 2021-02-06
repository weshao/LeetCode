#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
# https://leetcode-cn.com/problems/candy/description/
#
# algorithms
# Hard (45.19%)
# Likes:    446
# Dislikes: 0
# Total Accepted:    59.6K
# Total Submissions: 123.9K
# Testcase Example:  '[1,0,2]'
#
# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
# 
# 你需要按照以下要求，帮助老师给这些孩子分发糖果：
# 
# 
# 每个孩子至少分配到 1 个糖果。
# 评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
# 
# 
# 那么这样下来，老师至少需要准备多少颗糖果呢？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[1,0,2]
# 输出：5
# 解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。
# 
# 
# 示例 2：
# 
# 
# 输入：[1,2,2]
# 输出：4
# 解释：你可以分别给这三个孩子分发 1、2、1 颗糖果。
# ⁠    第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
# 
#
from typing import List
# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        
        # greedy = [1 for _ in range(len(ratings))]
        # for i in range(1, len(ratings)):
        #     if ratings[i] > ratings[i-1]:
        #         greedy[i] = greedy[i-1] + 1
        # for i in range(len(ratings)-2, -1, -1):
        #     if ratings[i] > ratings[i+1]:
        #         greedy[i] = max(greedy[i], greedy[i+1] + 1)
        # return sum(greedy)
        all = 1
        pre = 1
        dec = 0
        inc = 1
        for i in range(1, len(ratings)):
            if ratings[i] >= ratings[i-1]:
                pre = (1 if ratings[i] == ratings[i-1] else pre+1)
                all += pre
                dec = 0
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                all += dec
                pre = 1

        
# @lc code=end
so = Solution()
ans = so.candy([1,2,3,2,0])
print(ans)
