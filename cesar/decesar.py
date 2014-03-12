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


def decrypt_cesar(tekst='', k0=0, k1=0, n=1):
    out = ''
    for i in range(len(tekst)):
        temp = ((ord(tekst[i])+(n - k0)) * k1) % n
        for j in range(euler(n) - 1 - 1):
            temp = (temp * temp) % n
        out += chr(temp + ord('a'))
    print(euler(20))
    return out
