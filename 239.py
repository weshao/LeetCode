class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_start = 0
        max_num = float('-inf')
        window = []

        for window_end in range(len(nums)):
            right_num = nums[window_end]
            max_num = max(max_num, right_num)
            if window_end >= k - 1:
                max = 
