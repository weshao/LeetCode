# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        last_node_of_previous = None
        last_node_of_sub = head
        while True:
            current = last_node_of_sub
            previous = last_node_of_previous
            i = 0
            while current is not None and i < k:
                next = current.next
                current.next = previous
                previous = current
                current = next
                i += 1
            
            if i == k:
                if last_node_of_previous is None:
                    head = previous
                else:
                    last_node_of_previous.next = previous
                
                last_node_of_sub.next = current
                last_node_of_previous = last_node_of_sub
                
                if current is None:
                    break

                last_node_of_sub = current
            else:
                current = previous
                previous = None
                while i:
                    next = current.next
                    current.next = previous
                    previous = current
                    current =next
                    i -= 1
                last_node_of_previous.next = previous
                break
                
        return head




problem = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

result = problem.reverseKGroup(head, 3)
print('done')