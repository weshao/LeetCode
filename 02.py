class ListNode:
    def __init__(self,x):
        self.val=x;
        self.next=None;
class Solution:
    def addTwoNumbers(self,l1:ListNode,l2:ListNode):
        p1=l1
        p2=l2
        p3=p4 =ListNode(0)
        flag=0
        while p1 or p2 or flag:
            p3.next = ListNode(flag + p1.val + p2.val)
            if p3.next.val>=10:
                flag=1
                p3.next.val-=10
            p3=p3.next
            p1=p1.next if p1.next else p1
            p2=p2.next if p2.next else p2
        return p4