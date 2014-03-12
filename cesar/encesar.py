def encrypt_cesar(tekst, k0, k1, n):
    out = ''
    for i in range(len(tekst)):
        out += chr(((ord(tekst[i]) * k1) + k0) % n + ord('a'))
    return out
