def czy_wiel(liczba1, liczba2):
    """

    :param liczba1:
    :param liczba2:
    :return:
    """
    if liczba1 % liczba2 == 0 or liczba2 % liczba1 == 0:
        return True
    else:
        return False


with open('PARY_LICZB.TXT') as file:
    licznik = 0
    for para in file:
        if int(para[0]) == 0 or int(para[1]) == 0:
            continue
        if czy_wiel(int(para[0]), (int(para[1]))):
            licznik += 1
print(licznik)
