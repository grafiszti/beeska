import constants


def fme(a, k, n):
    b = bin(k)[2:] # list of bits
    m = len(b)
    r = 1 # result
    x = a % n

    for i in range(m - 1, -1, -1):
        if b[i] == '1':
            r = r * x % n

        x **= 2
        x %= n

    return r


def hcf(n1, n2):
  while n1*n2:
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
    euler_number = euler(len(constants.alphabet))
    for i in range(len(tekst)):
        if tekst[i] in constants.alphabet:
            temp = constants.alphabet.index(tekst[i])
            out += constants.alphabet[fme(((temp + len(constants.alphabet) - k0) * k1),
                                              (euler_number - 1),
                                              len(constants.alphabet))]
        else:
            out += ' '
    return out