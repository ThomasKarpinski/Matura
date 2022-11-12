i = 0
n = len(d)
maks = 0
for i in range(1, n):
    if wieksze(i, maks):
        maks = i
print(maks)