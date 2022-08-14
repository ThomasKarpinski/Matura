print("Witaj użytkowniku")


def szyfr(tekst, klucz, operacja):
    wynik = ""
    for i in range(len(tekst)):
        znak = tekst[i]
        if operacja == "kodowanie":
            if znak.isupper():
                wynik += chr(((ord(znak) - 65) + klucz) % 26 + 65)
            else:
                wynik += chr(((ord(znak) - 97) + klucz) % 26 + 97)
        else:
            if znak.isupper():
                wynik += chr(((ord(znak) - 65) - klucz) % 26 + 65)
            else:
                wynik += chr(((ord(znak) - 97) - klucz) % 26 + 97)
    return wynik


print(szyfr(tekst=input("Podaj tekst: "), klucz=int(input("Podaj klucz: ")), operacja=input("Jaka operacja? ")))
