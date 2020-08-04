class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = - x
            y = list(str(x))
            y.reverse()
            while y[0] == '0':
                y.pop(0)
            z = ''.join(y)
            z = - int(z)
        elif x == 0:
            z = 0
        else:
            y = list(str(x))
            y.reverse()
            while y[0] == '0':
                y.pop(0)
            z = ''.join(y)
            z = int(z)

        if z < -2 **31 or z > 2 **31 - 1:
            z = 0
        return z




