class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = []
        p = []
        z = []
        a = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                p.append(nums[i])
            elif nums[i] < 0:
                n.append(nums[i])

            if nums[i] == 0:
                z.append(nums[i])

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                if - (p[i] + p[j]) in n and [p[i], p[j], - (p[i] + p[j])] not in a:
                    a.append([p[i], p[j], - (p[i] + p[j])])

        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                if - (n[i] + n[j]) in p and [n[i], n[j], - (n[i] + n[j])] not in a:
                    a.append([n[i], n[j], - (n[i] + n[j])])

        if len(z) >= 3:
            a.append([0, 0, 0])

        return a
