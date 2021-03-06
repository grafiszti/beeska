from constants import alphabet


def decrypt_vig(tekst='', k=''):
    "funkcja deszyfrująca tekst z kodu vigenera, w petli,"
    "pobiera id kazdej literki z tekstu i zmienia go o"
    "id literki klucza(odejmuje) na odpowiednim miejscu w kluczu"
    "korzystając z mod dlugosc klucza, jesli wyjdziemy poza"
    "zakres alfabetu to mamy mod dlugosc alfabetu ktora zmienia"
    "id na id znaku w alfabecie"
    "zwracany jest odszyfrowany cjąg znakow"
    out = ''
    for i in range(len(tekst)):
        if tekst[i] in alphabet:
            out += alphabet[(alphabet.index(tekst[i]) - alphabet.index(k[i % len(k)])) % len(alphabet)]
        else:
            out += ' '
    return out