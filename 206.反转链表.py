#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # prev = None
        # while head is not None:
        #     next = head.next
        #     head.next = prev
        #     prev = head
        #     head = next
        # return prev
        if head is None or head.next is None:
            return head
        
        curl = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return curl


# @lc code=end

