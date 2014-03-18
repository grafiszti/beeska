import constants


def hcf(n1, n2):
    "funkcja obliczająca największy wspólny dzielnik"
    while n1 * n2:
        if n1 > n2:
            n1 %= n2
        else:
            n2 %= n1
    return max(n1, n2)


def coprime(n1, n2):
    "funkcja sprawdza czy największym wspolnym dzielnikiem jest 1"
    return hcf(n1, n2) == 1


def euler(number):
    "funkcja oblicza funkcję eulera dla podanej liczby"
    "w pętli przechodzi przez liczby od 0 do n i sprawdza"
    "czy ich NWD jest rowny 1"
    ret = 0
    for i in range(number):
        if coprime(i, number):
            ret += 1
    return ret


def decrypt_cesar(tekst='', k0=0, k1=0):
    "funkcja dekodująca szyfr cesara, jako parametry przekazujemy do niej"
    "zaszyfrowany text i dwa klucze które muszą byc względnie pierwsze z"
    "długością alfabetu uzytego do szyfrowania"
    out = ''
    n = len(constants.alphabet)
    euler_number = euler(n)
    for i in range(len(tekst)):
        if tekst[i] in constants.alphabet:
            temp = (constants.alphabet.index(tekst[i]) + n - k0)
            temp2 = k1
            for j in range(euler_number - 2):
                temp2 = (temp2 * k1) % n
            temp = (temp * temp2) % n
            out += constants.alphabet[temp]
        else:
            out += ' '
    return out