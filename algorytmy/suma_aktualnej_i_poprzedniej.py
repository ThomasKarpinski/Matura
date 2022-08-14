l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
i = 0
x = 0
while i <= 10:
    for j in l:
        x = l[j] + l[j + 1]
        print(x)
    i += 1
