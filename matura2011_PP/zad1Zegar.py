s = 5400
count = 0
while s > 0:
    r = s % 2
    if r == 1:
        count += 1
    s //= 2
print(count)
