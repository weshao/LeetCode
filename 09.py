class Solution:
    def isPalindrome(self, x: int) -> bool:
        flag = False
        if x >= 0:
            y = list(str(x))

            if len(y) == 1:
                flag = True
            else:
                while len(y) > 1:
                    flag = True
                    if y[0] == y[-1]:
                        y.pop(0)
                        y.pop(-1)
                    else:
                        flag = False
                        break
        return flag





