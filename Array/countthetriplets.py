class Solution:
    def countTriplet(self, arr, n):
        arr.sort()
        res = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr)-1):
                if arr[i] + arr[j] in arr:
                    res += 1
                if arr[i] + arr[j] > arr[-1]:
                    break
        
        return res


so = Solution()
ans = so.countTriplet([12, 8, 2, 11, 5, 14, 10], 7)
print(ans)