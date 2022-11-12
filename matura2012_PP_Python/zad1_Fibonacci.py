k = 8
l = [1, 1]
for i in range(2, k + 1):
    if i % 2 == 0:
        l.append(l[i - 1] + l[i - 2] + l[i - 3])
    else:
        l.append(l[i - 1])
print(l[-2])
