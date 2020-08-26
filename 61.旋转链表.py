#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head
        n = 0
        l1, l2 = head, head
        while l1:
            n += 1
            l1 = l1.next


        location = n - (k % n)
        if n <= 1 or location == n:
            return head
        while location > 1:
            l2 = l2.next
            location -= 1
        

        newhead = l2.next
        l2.next = None
        l2 = newhead
        while l2.next:
            l2 = l2.next
        l2.next = head
        return newhead

# @lc code=end
node = ListNode(1)
node.next = ListNode(1)
test = Solution()
ans = test.rotateRight([], 0)
print(ans)
