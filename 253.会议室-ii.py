import heapq
from typing import List
from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        allRoom = []
        intervals.sort(key = lambda x: x[0])
        for interval in intervals:
            if allRoom == []:
                heappush(allRoom, interval[1])
            else:
                if allRoom[0] <= interval[0]:
                    heappop(allRoom)
                heappush(allRoom, interval[1])
        return len(allRoom)

so = Solution()
ans = so.minMeetingRooms([[4,5],[2,3],[2,4],[3,5]])
print(ans)
