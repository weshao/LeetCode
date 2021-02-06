#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (59.65%)
# Likes:    492
# Dislikes: 0
# Total Accepted:    76.2K
# Total Submissions: 127.9K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 示例 1:
# 
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 
# 示例 2:
# 
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head:
            fast, slow = head, head
            while True:
                if fast.next is None or fast.next.next is None:
                    break
                fast = fast.next.next
                slow = slow.next
            
            rev = slow.next
            pre = None
            while rev:
                next = rev.next
                rev.next = pre
                pre = rev
                rev = next
            slow.next = pre

            start = head
            while pre:
                next = start.next
                start.next = pre
                pre = pre.next
                if pre:
                    start.next.next = next
                    start = next
                if not pre:
                    if next is slow:
                        next.next = None
                        start.next.next = next

            # return head
# @lc code=end
node = ListNode(1)
# node.next = ListNode(2)
# node.next.next = ListNode(3)
# node.next.next.next = ListNode(4)
# node.next.next.next.next = ListNode(5)
so = Solution()
ans = so.reorderList(node)
print(ans)