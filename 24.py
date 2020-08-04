# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#  
# 示例:
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        current, previous = head, None
        while True:
            last_node_of_previous_part = previous
            last_node_of_sub_list = current
            next = None
            i = 0
            while current is not None and i < 2:
                next = current.next
                current.next = previous
                previous = current
                current = next
                i += 1

            if last_node_of_previous_part is None:
                head = previous
            else:
                last_node_of_previous_part.next = previous #把前一个的最后和现在的最前面连在一起
            last_node_of_sub_list.next = current
            
            if current is None:
                break
            previous = last_node_of_sub_list
        return head
            





problem = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

result = problem.swapPairs(head)
print('done')