#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode-cn.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (46.85%)
# Likes:    516
# Dislikes: 0
# Total Accepted:    126.3K
# Total Submissions: 269.5K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 删除链表中等于给定值 val 的所有节点。
# 
# 示例:
# 
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.




class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        start = ListNode(0)
        start.next = head
        newstart = start
        while start and start.next:
            next = start.next
            while next and next.val == val:
                next = next.next
            start.next = next
            start = next
        return newstart.next




# @lc code=end

