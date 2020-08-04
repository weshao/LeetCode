class Solution:
    def threeSumClosest(self, nums, target):
# target = 1
# nums = [-1, 2, 1, -4]
        nums = sorted(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            s = i + 1
            e = len(nums) - 1
            while s < e:
                sum = nums[i] + nums[s] + nums[e]
                if abs(sum - target) < abs(ans - target):
                    ans = sum
                if sum > target:
                    e = e - 1
                elif sum < target:
                    s = s + 1
                elif sum == target:
                    return target
        return ans




#
# target = 1
# sum = []
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         for k in range(j+1, len(nums)):
#             # if (i != j and i != k and j!=k):
#             sum.append(nums[i] + nums[j] + nums[k] - target)
# sum_new = list(map(abs, sum))
# index = sum_new.index(min(sum_new))
# ans = sum[index] + target
#         # return ans
#
A = Solution()
ans = A.threeSumClosest([-1, 2, 1, -4], 1)