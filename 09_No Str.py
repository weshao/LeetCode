x = -121
while x > 0:
    x2 = x
    flag = 0
    while x // 10:
        x = x // 10
        flag += 1

    y = 0
    x = x2

    y =(x // 10**flag)
    while x // 10:

        y = y + (x % 10) * 10**flag
        x = x // 10
        flag -= 1





ß



print(flag)




