class Solution:
    def intToRoman(self, num: int) -> str:
        R = []
        # 1000: M
        if num // 1000:
            R.append("M" * (num // 1000))
            num = num % 1000
        # 500: D
        if num // 100 == 9:
            R.append("CM")
            num = num % 100
        elif num // 100 == 4:
            R.append("CD")
            num = num % 100
        elif num // 100:
            if num // 500:
                a = num // 100 - 5
                num = num % 100
                R.append("D" + 'C' * a)
            else:
                a = num // 100
                num = num % 100
                R.append('C' * a)

        10 - 100

        if num // 10 == 9:
            R.append("XC")
            num = num % 10
        elif num // 10 == 4:
            R.append("XL")
            num = num % 10
        elif num // 10:
            if num // 50:
                a = num // 10 - 5
                num = num % 10
                R.append("L" + 'X' * a)
            else:
                a = num // 10
                num = num % 10
                R.append('X' * a)

        if num == 9:
            R.append("IX")
        elif num == 4:
            R.append("IV")

        elif num:
            if num // 5:
                a = num - 5
                R.append("V" + 'I' * a)
            else:
                a = num
                R.append('I' * a)

        r = ''.join(R)
        return r
