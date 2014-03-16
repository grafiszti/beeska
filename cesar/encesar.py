import constants


def encrypt_cesar(tekst, k0, k1):
    out = ''
    for i in range(len(tekst)):
        out += constants.alphabet[((constants.alphabet.index(tekst[i]) * k1) + k0) % len(constants.alphabet)]
    return out
