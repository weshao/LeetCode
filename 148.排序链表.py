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

""" class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def divid_and_merge(head):
            if not head.next:
                return head
            
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            temp = slow.next
            slow.next = None
            left = divid_and_merge(head)
            right = divid_and_merge(temp)

            dumpHead = ListNode(0)
            rdumpHead = dumpHead
            while left and right:
                if left.val < right.val:
                    dumpHead.next = left
                    left = left.next
                else:
                    dumpHead.next = right
                    right = right.next
                dumpHead = dumpHead.next
            dumpHead.next = left if left else right

            return rdumpHead.next
        
        return divid_and_merge(head) if head else None """

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        while h:
            length += 1
            h = h.next
        res = ListNode(0)
        res.next = head
        while intv < length:
            pre, h = res, res.next
            while h:
                h1, i = h, intv
                while i and h:
                    h, i = h.next, i- 1
                if i:
                    break
                h2, i = h, intv
                while i and h:
                    h, i  = h.next, i - 1
                c1, c2 = intv, intv - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next = h1
                        h1 = h1.next
                        c1 = c1 - 1
                    else:
                        pre.next = h2
                        h2 = h2.next
                        c2 = c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre = pre.next
                    c1 = c1 - 1
                    c2 = c2 - 1
                pre.next = h
            intv *= 2
        return res.next
# @lc code=end
node = ListNode(4)
node.next = ListNode(3)
node.next.next = ListNode(2)
node.next.next.next = ListNode(6)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = ListNode(7)
node.next.next.next.next.next.next = ListNode(1)
so = Solution()
ans = so.sortList(node)
print(ans)
