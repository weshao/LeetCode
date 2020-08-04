class Solution:
    def maxSubArray(self, nums):
        if nums == []:
            return None
        else:
            # sum = 0
            # for num in nums:
            #     sum += num
            # left = 0
            # right = len(nums) - 1
            # m = sum
            # while left < right:
            #     # if nums[left] <= 0:
            #     #
            #     #     sum -= nums[left]
            #     #     left += 1
            #     #     if sum > m:
            #     #         m = sum
            #     #
            #     # elif nums[right] <= 0:
            #     #
            #     #     sum -= nums[right]
            #     #     right -= 1
            #     #     if sum > m:
            #     #         m = sum
            #
            #     if nums[left] < nums[right]:
            #         sum -= nums[left]
            #         left += 1
            #         if sum > m:
            #             m = sum
            #
            #     elif nums[left] > nums[right]:
            #         sum -= nums[right]
            #         right -= 1
            #         if sum > m:
            #             m = sum
            #
            #     elif nums[left] == nums[right]:
            #         if left <= right - 1:
            #             if nums[left+1] > nums[right-1]:
            #                 sum -= nums[right]
            #                 right -= 1
            #             else:
            #                 sum -= nums[left]
            #                 left += 1
            #
            #
            #
            # return m
            dp=[0]*len(nums)
            dp[0] = nums[0]
            for i in range(1,len(nums)):
                dp[i] = max(dp[i-1] + nums[i], nums[i])
            return max(dp)


i = Solution()
a = i.maxSubArray([2,3,-6,2,4])