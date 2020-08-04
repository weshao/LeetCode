class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def check(self, lists):
        if any(lists):
            for i in range(len(lists)):
                if lists[i]:
                    minl = lists[i].val
                    return True, minl, i
            return False
        else:
            return False, None, None

    def mergeKLists(self, lists):
        if any(lists):
            minl = lists[0].val
            l = 0
            for i in range(len(lists)):
                if lists[i].val:
                    if  lists[i].val < minl:
                        minl = lists[i].val
                        l = i
            res = ListNode(minl)
            ans = res
            if lists[l]:
                lists[l] = lists[l].next


            flag , minl , l= self.check(lists)
            while flag:
                for i in range(len(lists)):

                    if lists[i]:
                        if  lists[i].val < minl:
                            minl = lists[i].val
                            l = i
                res.next = ListNode(minl)
                res = res.next
                if lists[l]:
                    lists[l] = lists[l].next
                flag , minl, l= self.check(lists)
            return ans
        else: 
            return ListNode(None)


a = ListNode(1)
# a.next = ListNode(4)
# a.next.next = ListNode(5)

# b = ListNode(1)
# b.next = ListNode(3)
# b.next.next = ListNode(4)

# c = ListNode(2)
# c.next = ListNode(6)

i = Solution()
ans = i.mergeKLists([a])
print(ans.val)
print(ans.next.val)