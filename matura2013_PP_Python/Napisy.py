with open("napisy.txt", "r") as plik:
    napisy = [i.strip() for i in plik]

    """a)"""
    parzyste = [i for i in napisy if len(i) % 2 == 0]
    print(len(parzyste))

    """b)"""
    equals = [i for i in napisy if i.count('0') == i.count('1')]
    print(len(equals))

    """c)"""
    zera = [i for i in napisy if i.count('0') == len(i)]
    jedynki = [i for i in napisy if i.count('1') == len(i)]
    print(f"Napisy z samymi zerami: {len(zera)}\n"
          f"Napisy z samymi jedynkami: {len(jedynki)}")

    """d)"""
    for i in range(17):
        print(f"Liczb {i} cyfrowych jest {len([z for z in napisy if len(z) == i])}")
