class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        days_set = set(days)
        max_day = days[-1]
        dp = [0] * (max_day + 1)
        for i in range(1, max_day + 1):
            if i not in days_set:
                dp[i] = dp[i - 1]
            else:
                dp_7 = 0 if i - 7 < 0 else dp[i - 7]
                dp_30 = 0 if i - 30 < 0 else dp[i - 30]
                dp[i] = min(dp[i - 1] + costs[0],
                            dp_7 + costs[1],
                            dp_30 + costs[2])

        return dp[-1]

i = Solution()
a = i.mincostTickets([1,4,6,7,8,20], [2, 7, 15])
print(a)