#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (76.02%)
# Likes:    440
# Dislikes: 0
# Total Accepted:    69K
# Total Submissions: 90.6K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
# 
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
# 
# 示例:
# 
# 给定的有序链表： [-10, -3, 0, 5, 9],
# 
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#

# @lc code=start
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# # # # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def dfs(head):
            if not head:
                return None
            count = 0
            count_head = head
            while count_head is not None:
                count_head = count_head.next
                count += 1
            if count <= 1:
                return TreeNode(head.val)
            else:
                mid = count // 2
                left = head
                while mid>1:
                    left = left.next
                    mid -= 1
                midNode = left.next
                left.next = None
                right = midNode.next
                tree = TreeNode(midNode.val)
                tree.left = dfs(head)
                tree.right = dfs(right)

                return tree
        return dfs(head) if head else None
            

        
# @lc code=end
node = ListNode(-10)
# node.next = ListNode(-3)
# node.next.next = ListNode(0)
# node.next.next.next = ListNode(5)
# node.next.next.next.next = ListNode(9)

so = Solution()
ans = so.sortedListToBST(node)
print(ans)