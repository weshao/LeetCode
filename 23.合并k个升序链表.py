#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
from heapq import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val
        
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        minHeap = []
        for root in lists:
            heappush(minHeap, root)
        
        resultHead, resultTail = None, None
        while minHeap:
            node = heappop(minHeap)
            if resultHead is None:
                resultHead, resultTail = node
            else:
                resultTail.next = node
                resultTail = resultTail.next
            if node.next is not None:
                heappush(minHeap, node.next)
        
        return resultHead
        
# @lc code=end

