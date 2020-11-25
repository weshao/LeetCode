# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    # def ReverseList(self, pHead):
    #     if pHead is None:
    #         return None
    #     if pHead.next is None:
    #         return pHead
    #     curl = self.ReverseList(pHead.next)
    #     pHead.next.next = pHead
    #     pHead.next = None

    #     return curl

    def ReverseList(self, pHead):
        if pHead is None:
            return None
        prev = None
        while pHead is not None:
            next = pHead.next
            pHead.next = prev
            prev = pHead
            pHead = next
        return prev

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
ans = sol.ReverseList(head)
print(ans)
