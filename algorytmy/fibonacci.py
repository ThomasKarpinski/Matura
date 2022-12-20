# iteracyjnie
'''num = int(input("Enter the number: "))
if num == 0:
    print(num)
elif num == 1:
    print(num)
else:
    f1 = 0
    f2 = 1
    for i in range(num - 1):
        f1, f2 = f2, f1 + f2
    print(f2)'''


# rekurencyjnie
def iteratively(num):
    if num == 0:
        return num
    elif num == 1:
        return num
    else:
        return iteratively(num - 1) + iteratively(num - 2)


print(iteratively(11))
