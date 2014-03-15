import constants


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
            out += constants.alphabet[pow(((temp + len(constants.alphabet) - k0) * k1),
                                          (euler_number - 1),
                                          len(constants.alphabet))]
        else:
            out += ' '
    return out