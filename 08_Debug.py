class Solution:
    def myAtoi(self, str: str) -> int:
        while str:
            A = list(str)
            B =[]
            flag = 0
            while A and A[0] == ' ':
                A.pop(0)
            while A:
                if A[0] == '-':
                    flag = 1
                    A.pop(0)
                elif A[0] == '+':
                    A.pop(0)
                while A and '0' <= A[0] <= '9':
                    B.append(A.pop(0))
                while B:
                    B = ''.join(B)
                    B = int(B)
                    if flag:
                        B = -B
                        if B < - 2 ** 31:
                            B = -2 ** 31
                    elif B > 2**31 -1:
                        B = 2**31 -1
                    return B
                return 0
            return 0
        return 0


