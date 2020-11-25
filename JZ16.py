class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        pHead3 = ListNode(0)
        head = pHead3
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                pHead3.next = pHead1
                pHead1 = pHead1.next
            else:
                pHead3.next = pHead2
                pHead2 = pHead2.next
            pHead3 = pHead3.next
        pHead3.next = pHead1 if pHead1 else pHead2
        return head.next

head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(5)

head2 = ListNode(2)
head2.next = ListNode(4)
head2.next.next = ListNode(6)
sol = Solution()
ans = sol.Merge(None, head2)
print(ans)
