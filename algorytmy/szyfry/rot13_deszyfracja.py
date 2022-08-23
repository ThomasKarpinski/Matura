w = input("Podaj wyraz do deszyfracji: ")
w = w.upper()
offset = 13
str = ""
for i in w:
    x = ord(i)
    if x >= 77:
        str += chr(x - offset)
    else:
        str += chr(x + offset)
print(str)
