# 面试题51. 数组中的逆序对
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组，求出这个数组中的逆序对的总数。

# 输入: [7,5,6,4]
# 输出: 5


class Solution:
    def reversePairs(self, nums):
        if len(nums) < 2:
            return 0
        else:
            count = 0
            for i in range(len(nums)-1):
                temp = nums[i+1: len(nums)]
                temp.sort()
                if nums[i] in temp:
                    lo = temp.index(nums[i])
                    count += lo
                elif temp[-1] < nums[i]:
                    count += len(temp)
                elif nums[i] > temp[0] and temp[-1] > nums[i]:
                    for j in range(len(temp)):
                        if temp[j] > nums[i]:
                            break
                        else:
                            count += 1
    
        return count









i = Solution()
# a = i.reversePairs([7, 5, 6, 4])
# b = i.reversePairs([6, 4])
c = i.reversePairs([1,3,2,3,1])