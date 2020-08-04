# class Solution:
#     def removeDuplicates(self, nums):
#         i = 1
#         n = len(nums)
#         while i < n:
#             while nums[i] == nums[i-1]:
#                 del nums[i]
#                 if len(nums) <= 1 or i >= len(nums) :
#                     break
#             i += 1
#             n = len(nums)
#         return len(nums)




# sol = Solution()
# ans = sol.removeDuplicates([1, 1, 2])
# print(ans)


class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i+1
                 
        




sol = Solution()
ans = sol.removeDuplicates([1, 1, 2, 2, 4, 5, 5])
print(ans)