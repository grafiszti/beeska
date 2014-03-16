import constants


def encrypt_cesar(tekst, k0, k1):
    out = ''
    for i in range(len(tekst)):
        if tekst[i] in constants.alphabet:
            out += constants.alphabet[((constants.alphabet.index(tekst[i]) * k1) + k0) % len(constants.alphabet)]
        else:
            out += ' '
    return out
