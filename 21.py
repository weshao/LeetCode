# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == []:
            return l2
        elif l2 == []:
            return l1
        if l1 and l2:
            if l1.val < l2.val:
                lnew = ListNode(l1.val)
                l1 = l1.next
            else:
                lnew = ListNode(l2.val)
                l2 = l2.next
            l = lnew
            while l1!= None and l2!= None:
                if l1.val < l2.val:
                    lnew.next = ListNode(l1.val)
                    lnew = lnew.next
                    l1 = l1.next
                else:
                    lnew.next = ListNode(l2.val)
                    lnew = lnew.next
                    l2 = l2.next
            while l1:
                lnew.next = ListNode(l1.val)
                lnew = lnew.next
                l1 = l1.next

            while l2:
                lnew.next = ListNode(l2.val)
                lnew = lnew.next
                l2= l2.next

            return l
        
            


        