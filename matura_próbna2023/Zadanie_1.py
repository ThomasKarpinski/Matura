with open("mecz.txt") as plik:
    m = [i for i in plik]
    mecze = m[0]

    """1.1"""
    licznik = 0
    for i in range(len(mecze) - 1):
        if mecze[i] != mecze[i - 1]:
            licznik += 1
    print(f"Rozgrywkę wygrała inna drużyna niż rozgrywkę poprzednią: {licznik} razy")

    """1.2"""
    a = 0
    b = 0
    for i in range(len(mecze) - 1):
        if mecze[i] == 'A':
            a += 1
        if mecze[i] == 'B':
            b += 1
        if (a == 1000 or b == 1000) and abs(a - b) >= 3:
            break

    if a > b:
        print(f"A {a}:{b}")
    else:
        print(f"B {b}:{a}")

    """1.3"""
    passy_A = []
    passy_B = []
    passa_A = 0
    passa_B = 0
    for i in range(len(mecze) - 1):
        if mecze[i] == mecze[i + 1]:
            if mecze[i + 1] == 'A':
                passa_A += 1
            if mecze[i + 1] == 'B':
                passa_B += 1
        passy_A.append(passa_A)
        passy_B.append(passa_B)
        if mecze[i] == mecze[i + 1]:
            passa_A = 0
            passa_B = 0
    #print(passy_B, passy_A)
