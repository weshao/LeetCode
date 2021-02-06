#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (51.26%)
# Likes:    1095
# Dislikes: 0
# Total Accepted:    122.4K
# Total Submissions: 238.1K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
 # '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
# 
# 
# 
# 实现 LRUCache 类：
# 
# 
# LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value)
# 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
# 
# 
# 
# 
# 
# 
# 进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
# 
# 
# 
# 示例：
# 
# 
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 0 
# 最多调用 3 * 10^4 次 get 和 put
# 
# 
#

# @lc code=start
class BiList():
  def __init__(self, key, val) -> None:
      super().__init__()
      self.key = str(key)
      self.val = val
      self.last = None
      self.next = None


# class LRUCache:

#     def __init__(self, capacity: int):
#       self.cap = capacity
#       self.inside = 0
#       self.ht = dict()
#       self.bl = BiList(0, 0)
#       self.bl.next = BiList(0, 0)
#       self.bl.next.last = self.bl
#       self.tail = self.bl.next



#     def get(self, key: int) -> int:
#       if str(key) in self.ht:
#           node = self.ht[str(key)]
#           node.last.next = node.next
#           node.next.last = node.last
#           node.next = self.bl.next
#           self.bl.next.last = node
#           self.bl.next = node
#           node.last = self.bl
#           return node.val
#       else:
#         return -1


#     def put(self, key: int, value: int) -> None:
#       if self.inside < self.cap:
#         if str(key) in self.ht:
#           node = self.ht[str(key)]
#           node.val = value
#           node.last.next = node.next
#           node.next.last = node.last
#           node.next = self.bl.next
#           self.bl.next.last = node
#           self.bl.next = node
#           node.last = self.bl
          
#         else:
#           node = BiList(key, value)
#           self.ht[str(key)] = node
#           node.next = self.bl.next
#           self.bl.next.last = node
#           self.bl.next = node
#           node.last = self.bl
#           self.inside += 1
#       elif self.inside >= self.cap:
#         if str(key) in self.ht:
#           node = self.ht[str(key)]
#           node.last.next = node.next
#           node.next.last = node.last
#           node.val = value
#           node.next = self.bl.next
#           self.bl.next.last = node
#           self.bl.next = node
#           node.last = self.bl
#         else:
#           node = BiList(key, value)
#           self.ht[str(key)] = node
#           node.next = self.bl.next
#           self.bl.next.last = node
#           self.bl.next = node
#           node.last = self.bl
#           denode = self.tail.last
#           denode.last.next = denode.next
#           denode.next.last = denode.last
#           del self.ht[denode.key]

from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)





          



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
obj = LRUCache(2)
obj.put(2,1)
obj.put(3,2)
param_1 = obj.get(2)
param_2 = obj.get(3)
obj.put(4,3)
param_3 = obj.get(2)
param_4 = obj.get(3)
param_5 = obj.get(4)
print("here")