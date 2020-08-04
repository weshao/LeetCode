
str1 = "woo"
str2 = "owl"
if len(str1) != len(str2):
    print('false')
str3 = ''
for ii in range(len(str1)):
    a =

    flag = False
    for jj in range(len(str2)):
        if str1[ii] == str2[jj]:
            flag = True
            str3 += str2[jj]
            break
    if not flag:
        print('false')
if str1 == str3:
    print('true')
else:
    print("false")