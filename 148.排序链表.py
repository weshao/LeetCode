#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
from typing import List

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         if head is None or head.next is None:
#             return head
#         slow, fast = head, head
#         while fast.next and fast.next.next:
#             slow = slow.next
#             fast = fast.next.next

#         left = head
#         right = slow.next
#         slow.next = None
#         sortedLeft = self.sortList(left)
#         sortedRight = self.sortList(right)
#         dummyHead = ListNode(0)
#         dummyHead2 = dummyHead
#         while sortedLeft and sortedRight:
#             if sortedLeft.val < sortedRight.val:
#                 dummyHead.next = sortedLeft
#                 sortedLeft = sortedLeft.next
#             else:
#                 dummyHead.next = sortedRight
#                 sortedRight = sortedRight.next
#             dummyHead = dummyHead.next
#         dummyHead.next = sortedRight if sortedRight else sortedLeft
#         return dummyHead2.next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        while h:
            h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        while intv < length:
            pre, h = res, res.next
            while h:
                h1, i = h, intv
                while i and h:
                    h, i = 

# @lc code=end
node = ListNode(-1)
node.next = ListNode(5)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(0)
so = Solution()
ans = so.sortList(node)
print(ans)
