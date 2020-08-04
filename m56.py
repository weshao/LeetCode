class Solution:
    def singleNumbers(self, nums):
        # result = []
        # for i in range(len(nums)):
        #     if i==0:
        #         if nums[i] not in nums[i+1:len(nums)]:
        #             result.append(nums[i])
        #     elif i==len(nums)-1:
        #         if nums[i] not in nums[0:len(nums)-1]:
        #             result.append(nums[i])
        #     else:
        #         if (nums[i] not in nums[0: i]) and nums[i] not in nums[i+1:len(nums)]:
        #             result.append(nums[i])
        #     if len(result)==2:
        #         break
        # return result

        ret = 0
        a = 0
        b = 0
        for i in range(len(nums)):
            ret ^= nums[i]
        
        low = 1
        while low & ret == 0:
            low <<= 1
        
        for n in nums:
            if n & low:
                a ^= n
            else:
                b ^= n
        return [a, b]






i = Solution()
a = i.singleNumbers([1,2,5,2]) 