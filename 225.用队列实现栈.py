#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
# https://leetcode-cn.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (66.38%)
# Likes:    266
# Dislikes: 0
# Total Accepted:    89.1K
# Total Submissions: 134.2K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# 使用队列实现栈的下列操作：
# 
# 
# push(x) -- 元素 x 入栈
# pop() -- 移除栈顶元素
# top() -- 获取栈顶元素
# empty() -- 返回栈是否为空
# 
# 
# 注意:
# 
# 
# 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty
# 这些操作是合法的。
# 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
# 
# 
#
from collections import deque
# @lc code=start
from collections import deque
# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque([])
        self.queue2 = deque([])

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        n = len(self.queue)
        self.queue2.append(x)
        for i in range(n):
            self.queue2.append(self.queue.popleft())
        self.queue = self.queue2
        self.queue2 = deque([])

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(5)
obj.push(4)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
# @lc code=end

