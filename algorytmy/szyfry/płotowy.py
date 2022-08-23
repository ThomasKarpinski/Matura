def encode(message: str, key: int) -> str:
    """
        :param message: wiadomość do zaszyfrowania
        :param key: klucz
        :return: zaszyfrowana wiadomość
        """
    encoded = ""

    for k in range(key):
        if k == key - 1:
            jump = (key - 1) * 2
        else:
            jump = (key - (k + 1)) * 2

        i = k

        while i < len(message):
            encoded += message[i]
            i += jump

    return encoded


message = "computer science"

encoded = encode(message, 3)

print(f"Encoded: {encoded}")
