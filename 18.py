class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums.sort()
        result = []
        for loop1 in range(len(nums) - 3):
            for loop2 in range(loop1+1, len(nums)-2):
                start = loop2 + 1
                end = len(nums) - 1
                while start < end:
                    if nums[loop1] + nums[loop2] + nums[start] + nums[end] == target:
                        if [nums[loop1], nums[loop2], nums[start],nums[end]] not in result:
                            result.append([nums[loop1], nums[loop2], nums[start],nums[end]])
                        start += 1
                        end -= 1
                    elif nums[loop1] + nums[loop2] + nums[start] + nums[end] < target:
                        start += 1
                    elif nums[loop1] + nums[loop2] + nums[start] + nums[end] > target:
                        end -= 1
        return result
        
I = Solution()
# a = I.fourSum([1, 0, -1, 0, -2, 2], 0)
# b = I.fourSum([0,0,0,0], 0)
a = I.fourSum([-3,-2,-1,0,0,1,2,3], 0)