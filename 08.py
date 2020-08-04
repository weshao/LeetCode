str = "   -91283472332"
A = list(str)
B =[]
flag = 0
while A[0] == ' ':
    A.pop(0)
if A[0] == '-':
    flag = 1
    A.pop(0)
while A and '0' <= A[0] <= '9':
    B.append(A.pop(0))
C = ''.join(B)
C = int(C)
if flag:
    C = -C
if C > 2**31 -1:
    C = 2**31 -1
if C < - 2**31:
    C = -2**31


