w = input("Podaj słowo do zaszyfrowania: ")
w = w.upper()
print(w)

offset = 13
string = ""

for i in w:
    x = ord(i)
    if x <= 77:
        string += chr(x + offset)
    elif x > 77:
        string += chr(x - offset)
print(string)