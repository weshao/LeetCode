class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = 1

        if len(height) == 2:
            v = min(height[0], height[1])

        else:
            while j < len(height) - 1:
                # bv = volume(i, j+1)
                bv = (j + 1 - i) * min(height[j + 1], height[i])
                # sv = volume(i+1, j+1)
                sv = (j + 1 - i - 1) * min(height[j + 1], height[i + 1])
                if bv > sv:
                    j += 1
                else:
                    i += 1
                    j += 1
            v = max(bv, sv)

        return v





