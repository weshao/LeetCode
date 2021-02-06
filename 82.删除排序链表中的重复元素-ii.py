#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (49.82%)
# Likes:    417
# Dislikes: 0
# Total Accepted:    78.4K
# Total Submissions: 157.2K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
# 
# 示例 1:
# 
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 
# 
# 示例 2:
# 
# 输入: 1->1->1->2->3
# 输出: 2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
from typing import NoReturn


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        newHead = ListNode(None)
        newHead.next = head
        saveHead = newHead
        breakHead = newHead
        newHead = newHead.next
        flag = None
        while newHead.next:
            if  newHead.val != newHead.next.val and newHead.val != flag:
                breakHead.next = newHead
                breakHead = newHead
                flag = newHead.val
                newHead = newHead.next
            else:
                flag = newHead.val
                newHead = newHead.next

        if newHead.val != flag:
            breakHead.next = newHead
            breakHead = newHead
        breakHead.next = None

        return saveHead.next


# @lc code=end
node = ListNode(1)
so = Solution()
ans = so.deleteDuplicates(node)
print(ans)

