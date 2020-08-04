class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         if head.next == None:
#             return None
#         else:
#             count = 1
#             i = head
#             while i.next != None:
#                 i = i.next
#                 count += 1
#             i = head
#             count2 = 1
#             if count == n:
#                 return head.next
#             else:
#                 while count2 < count - n:
#                     i = i.next
#                     count2 += 1
#                 i.next = i.next.next
#                 return head

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None
        else:
            count = 1
            i = head
            j = head
            while i.next != None:
                i = i.next
                count += 1
                if count > n:
                    j = j.next
            if count == n:
                return head.next
            else:
                j.next = j.next.next
                return head