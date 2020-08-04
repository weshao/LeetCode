class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        self.array = mountain_arr
        self.t = target
        length = len(mountain_arr)
        left = 0
        right = length - 1
        ans = self.find(left,right)
        if ans != None:
            return ans
        else:
            return -1  


    def find(self, left, right):
        mid = (left + right) //2
        a = self.array[mid-1]
        b = self.array[mid]
        c = self.array[mid+1]
        if a<b and b>c:
            if b < self.t:
                return -1
            elif b == self.t:
                return mid
            else:
                dd = self.findleft(left, mid)
                if dd != None:
                    return dd
                ee = self.findright(mid, right)
                if ee != None:
                    return ee
        elif a<b and b<c:
            a = self.findleft(left, mid)
            if a != None:
                return a
            else:
                gg = self.find(mid, right)
                if gg!= None:
                    return gg
        elif a>b and b>c:
            ff = self.find(left,mid)
            if ff != None:
                return ff
            bb = self.findright(mid, right)
            if bb != None:
                return bb
            






    def findleft(self, left, right):
        
        while left <= right:
            mid = (left + right)//2
            d = self.array[mid]
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
            d = self.array[mid]
            if d == self.t:
                return mid
            elif d > self.t:
                left = mid+1

            elif d < self.t:
                right = mid-1


i =Solution()
a = i.findInMountainArray(0, [3,5,3,2,0])
print(a)