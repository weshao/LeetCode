height = [1,8,6,2,5,4,8,3,7]


# def volume(i, j):
#     f = height[i]
#     e = height[j]
#     v = (j - i) * min(f, e)
#     return v
# v = 0
# if len(height) == 2:
#     v = min(height[0], height[1])
#
#
# else:
#     while i < len(height) - 1:
#         # bv = volume(i, j+1)
#         bv = (j + 1 - i) * min(height[j+1], height[i])
#         # sv = volume(i+1, j+1)
#         sv = (j + 1 - i - 1) * min(height[j + 1], height[i + 1])
#         if bv >= sv:
#             j += 1
#         else:
#             i += 1
#             j += 1
#
#         v = max(v, bv, sv)
#         if j == len(height) - 1:
#             i = i + 1
#             j = i
# v = 0
# while len(height) > 1:
#     a = height.pop(0)
#     h2 = height[:]
#     # ind = 0
#     b = max(h2)
#     ind = h2.index(b)
#     v = max(v, (ind + 1) * min(a, b))
#     while ind < len(height) -1:
#         b = max(h2[ind+1:])
#         ind2 = h2[ind+1:].index(b) + ind + 1
#         ind = ind2
#         v = max(v, (ind + 1) * min(a, b))

        # ind += 1

# v = []
# for i in range(len(height)):
#     for j in range(i, len(height)):
#         v.append(abs(j-i)*min(height[i], height[j]))
#
# vmax = max(v)


v = 0
i = 0
j = len(height)-1
# v = (j-i) * min(height[i], height[j])
while j - i >= 1:
    v = max(v, (j - i) * min(height[i], height[j]))
    if height[i] < height [j]:
        i += 1
    else:
        j -= 1





