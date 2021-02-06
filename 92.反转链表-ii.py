#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (51.82%)
# Likes:    619
# Dislikes: 0
# Total Accepted:    93.3K
# Total Submissions: 179.8K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n or not head:
            return head
        i = 1
        saveHead = head
        while head:
            if i == m-1:
                lastTail = head
                head = head.next
                i += 1
            elif i < m - 1:
                head = head.next
                i += 1
            elif i == m:
                tail = head
                next = head.next
                prev = head
                head = next
                i += 1
            elif m < i < n:
                next = head.next
                head.next = prev
                prev = head
                head = next
                i += 1
            elif i == n:
                next = head.next
                head.next = prev
                tail.next = next
                if m > 1:
                    lastTail.next = head
                    return saveHead
                elif m == 1:
                    return head

# @lc code=end
node = ListNode(1)
node.next = ListNode(2)
# node.next.next = ListNode(3)
# node.next.next.next = ListNode(4)
# node.next.next.next.next = ListNode(5)
so = Solution()
ans = so.reverseBetween(node, 1, 2)
print([ans])
