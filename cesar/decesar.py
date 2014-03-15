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
    euler_number = euler(len(constants.alphabet)) - 1
    for i in range(len(tekst)):
        if tekst[i] in constants.alphabet:
            temp = constants.alphabet.index(tekst[i])
            temp = ((temp + (len(constants.alphabet) - k0)) * k1) % len(constants.alphabet)
            temp2 = temp
            for j in range(euler_number):#jak cos to mozna odjac 1 od euer_number bo nie wiem czy to tak nie powinno byc
                temp2 = (temp2 * temp) % len(constants.alphabet)
            out += constants.alphabet[temp2]
        else:
            out += ' '
    return out