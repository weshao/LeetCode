#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (51.74%)
# Likes:    441
# Dislikes: 0
# Total Accepted:    168.1K
# Total Submissions: 324.8K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 
# 示例 1:
# 
# 输入: 1->1->2
# 输出: 1->2
# 
# 
# 示例 2:
# 
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        oldhead = head
        while head.next is not None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return oldhead
# @lc code=end
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(2)
node.next.next.next = ListNode(3)
node.next.next.next.next = ListNode(3)
so = Solution()
ans = so.deleteDuplicates(node)
print(ans)
