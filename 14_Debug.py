strs = ["ac","acc","accc"]
strs.sort(key=len)

l = []

s = []
for i in range(len(strs)):
    s.append(list(strs[i]))

while s[0]:
    f = s[0].pop(0)
    m = 0
    for i in range(1, len(s)):
        if f == s[i][0]:
            s[i].pop(0)
            m += 1
    if m == len(s) - 1:
        l.append(f)
    else:
        break
