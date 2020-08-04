class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        new = []
        while nums1 or nums2:
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    new.append(nums1.pop(0))
                else:
                    new.append(nums2.pop(0))
            elif nums1 and not nums2:
                # new.extend(nums1.pop(0))
                new.extend(nums1)
                nums1 = []
            elif nums2 and not nums1:
                # new.append(nums2.pop(0))
                new.extend(nums2)
                nums2 = []
        if len(new)%2 == 1:
            return new[int ((len(new) - 1) / 2)]
        if len(new) % 2 == 0:
            return (new[int(len(new) / 2) - 1] + new[int(len(new) /  2)]) / 2


sh = Solution()
a = sh.findMedianSortedArrays([1,2],[3,4])


