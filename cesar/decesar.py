import constants


def hcf(n1, n2):
    while n1 * n2:
        if n1 > n2:
            n1 %= n2
        else:
            n2 %= n1
    return max(n1, n2)


def coprime(n1, n2):
    return hcf(n1, n2) == 1


def euler(number):
    ret = 0
    for i in range(number):
        if coprime(i, number):
            ret += 1
    return ret


def decrypt_cesar(tekst='', k0=0, k1=0):
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