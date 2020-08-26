#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        l3 = ListNode(0)
        head = l3
        while l1 or l2:
            if l1 is None:
                l1Num = 0
            else:
                l1Num =l1.val
            if l2 is None:
                l2Num = 0
            else:
                l2Num =l2.val

            num = (l1Num + l2Num + flag) % 10
            flag = (l1Num + l2Num + flag) // 10
            l3.next = ListNode(num)
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            l3 = l3.next
            if l1 is None and l2 is None and flag == 1:
                l3.next = ListNode(1) 
        return head.next
# @lc code=end
l1 = ListNode(1)


l2 = ListNode(9)
l2.next = ListNode(9)

test = Solution()
ans = test.addTwoNumbers(l1, l2)
print(ans)
