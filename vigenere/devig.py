from constants import alphabet


def decrypt_vig(tekst='', k=''):
    out = ''
    for i in range(len(tekst)):
        if tekst[i] in alphabet:
            out += alphabet[(alphabet.index(tekst[i]) - alphabet.index(k[i % len(k)])) % len(alphabet)]
        else:
            out += ' '
    return out