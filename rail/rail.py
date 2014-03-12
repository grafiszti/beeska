def rail(tekst='', en=1):
    out = ''
    if en == 1:
        return tekst
    for i in range(en):
        l_dol = list(range(i, len(tekst), (2 * en) - 2))
        l_gora = list(range((2 * en) - 2 - i, len(tekst), (2 * en) - 2))
        lista = list(set(l_dol + l_gora))
        lista.sort()
        for it in lista:
            out += tekst[it]
    return out

