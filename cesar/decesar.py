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


alphabet = {'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y',
            'z'}


def index_of(table={'a'}, element_to_check='b'):
    for i in range(len(table)):
        if table[i] == element_to_check:
            return i
    return -1


def decrypt_cesar(tekst='', k0=0, k1=0, n=1):
    out = ''
    euler_number = euler(n)
    for i in range(len(tekst)):
        temp = index_of(alphabet, tekst[i])
        if temp != -1:
            temp = (temp + (len(alphabet) - k0)) * k1
            temp2 = 1
            for j in range(euler_number):#jak cos to mozna odjac 1 od euer_number bo nie wiem czy to tak nie powinno byc
                temp2 = temp2 * temp % len(alphabet)
            out += alphabet[temp2]
        elif temp == -1:
            out += ' '
    return out