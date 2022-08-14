# iteracyjnie
'''num = int(input("Enter the number: "))
if num == 0:
    print(num)
elif num == 1:
    print(num)
else:
    s=1
    for i in range(1, num+1):
        s *= i
    print(s)'''


# rekurencyjnie
def factorial(num):
    if num == 0:
        return num
    elif num == 1:
        return num
    else:
        return num * (factorial(num - 1))


print(factorial(5))
