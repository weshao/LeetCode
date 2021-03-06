#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (57.13%)
# Likes:    926
# Dislikes: 0
# Total Accepted:    180.7K
# Total Submissions: 315.4K
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3'
#
# 编写一个程序，找到两个单链表相交的起始节点。
# 
# 如下面的两个链表：
# 
# 
# 
# 在节点 c1 开始相交。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2,
# skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为
# [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
# 
# 
# 
# 
# 示例 2：
# 
# 
# 
# 输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB =
# 1
# 输出：Reference of the node with value = 2
# 输入解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为
# [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
# 
# 
# 
# 
# 示例 3：
# 
# 
# 
# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为
# 0，而 skipA 和 skipB 可以是任意值。
# 解释：这两个链表不相交，因此返回 null。
# 
# 
# 
# 
# 注意：
# 
# 
# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        length_a, length_b = 0, 0
        
        headA_1, headB_1 = headA, headB
        while headA_1:
            length_a += 1
            headA_1 = headA_1.next
        while headB_1:
            length_b += 1
            headB_1 = headB_1.next
        
        if length_b > length_a:
            diff = length_b - length_a
            while diff:
                headB = headB.next
                diff -= 1
            
            while headB:
                if headB is headA:
                    return headB
                headB = headB.next
                headA = headA.next
        
        else:
            diff = length_a - length_b
            while diff:
                headA = headA.next
                diff -= 1
            
            while headA:
                if headB is headA:
                    return headA
                headB = headB.next
                headA = headA.next
        
        return None
            
# @lc code=end
headA = ListNode(4)
# headA.next = ListNode(1)
# headA.next.next = ListNode(8)
# headA.next.next.next = ListNode(4)
# headA.next.next.next.next = ListNode(5)

headB = ListNode(5)
headB.next = ListNode(0)
headB.next.next = headA
# headB.next.next.next = headA.next.next

so = Solution()
ans = so.getIntersectionNode(headA, headB)
print(ans)
