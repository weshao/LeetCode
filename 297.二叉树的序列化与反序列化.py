#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#
# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (53.32%)
# Likes:    450
# Dislikes: 0
# Total Accepted:    63.7K
# Total Submissions: 119.4K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# 
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
# 
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 /
# 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
# 
# 示例: 
# 
# 你可以将以下二叉树：
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠    / \
# ⁠   4   5
# 
# 序列化为 "[1,2,3,null,null,4,5]"
# 
# 提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode
# 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
# 
# 说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
# 
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return str(res)
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(None)
        return str(res)
        

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if eval(data) == []:
            return None
        treelist = deque(eval(data))
        root = TreeNode(treelist[0])
        treelist.popleft()
        queue = deque([root])
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                left = TreeNode(treelist.popleft())
                if left.val != None:
                    node.left = left
                    queue.append(left)
                right = TreeNode(treelist.popleft())
                if right.val != None:
                    node.right = right
                    queue.append(right)
        return root







# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(0)
tree.right = TreeNode(3)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(5)
so = Codec()
ans = so.serialize(tree)
print(ans)
ans2 = so.deserialize(ans)
print(ans2)