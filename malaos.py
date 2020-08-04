def compare(str1, str2):
    if len(str1) != len(str2):
        return False
    a = 0
    b = 0
    for i in range(len(str1)):
        a = a + ord(str1[i])
        b = b + ord(str2[i])
    if a == b:
        return True
    else:
        return False


# strs = ['woo', 'owl']
strs = ["ray","cod","abe","ned","arc","jar","owl","pop","paw","sky","yup","fed","jul","woo","ado","why","ben","mys","den","dem","fat","you","eon","sui","oct","asp","ago","lea","sow","hus","fee","yup","eve","red","flo","ids","tic","pup","hag","ito","zoo"]
res = [[strs[0]]]
N = len(strs)
for c in range(1, N):
    x = 0
    for i in range(len(res)):
        a, b = strs[c], res[i][-1]
        if compare(a, b):
            if compare(b, a):
                print(strs[c], res[i][-1])
                x = i
        else:
            continue
    if x:
        res[x].append(strs[c])
    else:
        res.append([strs[c]])


