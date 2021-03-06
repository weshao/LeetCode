class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            A = [[0 for t in range(len(s))] for f in range(numRows)]
            S = list(s)
            i = 0
            j = 0
            flag = 1
            while S:
                A[i][j] = S.pop(0)
                if flag:
                    if i < numRows - 1:
                        i += 1
                    elif i == numRows - 1:
                        i -= 1
                        flag = 0
                        j += 1
                elif flag == 0:
                    if i > 0:
                        i -= 1
                        j += 1
                    elif i == 0:
                        flag = 1
                        i += 1
            B = []
            for m in range(numRows):
                for n in range(len(s)):
                    if A[m][n] != 0:
                        B.append(A[m][n])
            C = ''.join(B)
            return C





