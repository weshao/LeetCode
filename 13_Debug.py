s_o = "MMMCDXC"
s = list(s_o)
s.reverse()
s.append(' ')
s.reverse()
n = 0
for i in range(len(s)):
    if s[i] == 'I':
        n += 1
    elif s[i] == 'V':
        if s[i-1] == 'I':
            n += 3
        else:
            n += 5
    elif s[i] == 'X':
        if s[i-1] == 'I':
            n += 8
        else:
            n += 10
    elif s[i] == 'L':
        if s[i-1] == 'X':
            n += 30
        else:
            n += 50
    elif s[i] == 'C':
        if s[i-1] == 'X':
            n += 80
        else:
            n += 100
    elif s[i] == 'D':
        if s[i-1] == 'C':
            n += 300
        else:
            n += 500
    elif s[i] == 'M':
        if s[i-1] == 'C':
            n += 800
        else:
            n += 1000






