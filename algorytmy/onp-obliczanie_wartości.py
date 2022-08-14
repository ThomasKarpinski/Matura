x = input("wprowadź wyrażenie ze spacjami: ")
a = []
b = {'+': lambda x, y: y + x, '-': lambda x, y: y - x, '*': lambda x, y: y * x, '/': lambda x, y: y / x,
     '^': lambda x, y: y ** x}
for c in x.split():
    if c in b:
        a.append(b[c](a.pop(), a.pop()))
    else:
        a.append(float(c))
    print(c, a)
