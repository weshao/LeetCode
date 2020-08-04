class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        self.array = mountain_arr
        self.t = target
        len = mountain_arr.length()
        left = 0
        right = len - 1
        ans = self.find(left,right)
        if ans  > -1:
            return ans
        else:
            return -1  


    def find(self, left, right):
        mid = (left + right) //2
        a = self.array.get(mid-1)
        b = self.array.get(mid)
        c = self.array.get(mid+1)
        if a<b and b>c:
            if b < self.t:
                return -1
            elif b == self.t:
                return mid
            else:
                cc = self.findleft(left, mid)
                if cc  > -1:
                    return cc
                dd = self.findright(mid, right)
                if dd  > -1:
                    return dd
        elif a<b and b<c:
            mm = self.findleft(left, mid)
            if mm  > -1:
                return mm
            else:
                self.find(mid, right)
        elif a>b and b>c:
            self.find(left,mid)
            nn = self.findleft(mid, right)
            if nn  > -1:
                return nn
            
            






    def findleft(self, left, right):
        
        while left <= right:
            mid = (left + right)//2
            d = self.array.get(mid)
            if d == self.t:
                return mid
            elif d > self.t:
                right = mid-1
                # mid = (mid + left) // 2
            elif d < self.t:
                left = mid+1
                # mid = (mid + right) // 2


    def findright(self, left, right):
        
        while left <= right:
            mid = (left + right)//2
            d = self.array.get(mid)
            if d == self.t:
                return mid
            elif d > self.t:
                left = mid+1
                # mid = (mid + right) // 2
            elif d < self.t:
                right = mid-1
                # mid = (mid + left) // 2