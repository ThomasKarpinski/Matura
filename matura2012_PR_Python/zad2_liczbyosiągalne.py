def zad2_c(n):
    """
    sprawdza czy liczba n jest osiągalna spełniając warunek n=k+s(k)
    :param n: liczba naturalna
    """
    if 1000 <= n <= 9999:
        for s in range(4, 33):
            k = n - s
            suma = k % 10 + (k // 10) % 10 + (k // 100) % 10 + (k // 1000) % 10
            if suma == s:
                return k
    return 0


wynik = zad2_c(9999)
print(wynik) if wynik != 0 else "NIE"
