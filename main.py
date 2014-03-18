from rail import rail, derail
from cesar import encesar, decesar
from vigenere import envig, devig


def main():
    menu = 99
    while True:
        if menu == 99:
            print('Wybierz operacje do wykonania:\n'
                  '1. rail\n'
                  '2. derail\n'
                  '3. szyfrowanie - przestawienie macierzowe\n'
                  '4. deszyfrowanie - przestawienie macierzowe\n'
                  '5. szyfrowanie - przestawienie macierzowe - zmienny klucz\n'
                  '6. deszyfrowanie - przestawienie macierzowe - zmienny klucz\n'
                  '8. deszyfrowanie cezara\n'
                  '9. szyrfowanie Vigenerea\n'
                  '10. deszyrfowanie Vigenerea\n'
                  '99. Wyswietlenie opcji\n'
                  'ctrl-c. wyjscie\n')
        menu = 0
        try:
            temp = input('> ')
        except KeyboardInterrupt:
            print('wyjscie')
            break
        try:
            menu = int(temp)
        except ValueError:
            print('blad!')
        if menu == 1:
            t1 = input('Tekst do zaszyfrowania: ').replace(' ', '_')
            n = 0
            while n==0:
                tn = input('Wartosc N: ')
                try:
                    n = int(tn)
                except ValueError:
                    print('blad')
            print('Wynik: ' + rail.rail(t1, n))
        if menu == 2:
            t1 = input('Tekst do odszyfrowania: ').replace(' ', '_')
            n = 0
            while n == 0:
                tn = input('Wartosc N: ')
                try:
                    n = int(tn)
                except ValueError:
                    print('blad')
            print('Wynik: ' + derail.derail(t1, n))
        if menu == 3:
            t1 = input('Tekst do zaszyfrowania: ').replace(' ', '_')
            n = 0
            while n==0:
                tn = input('Wartosc N: ')
                try:
                    n = int(tn)
                except ValueError:
                    print('blad')
            print('Wynik: ' + rail.rail(t1, n))
        if menu == 4:
            t1 = input('Tekst do odszyfrowania: ').replace(' ', '_')
            n = 0
            while n == 0:
                tn = input('Wartosc N: ')
                try:
                    n = int(tn)
                except ValueError:
                    print('blad')
            print('Wynik: ' + derail.derail(t1, n))
        if menu == 5:
            t1 = input('Tekst do zaszyfrowania: ').replace(' ', '_')
            n = 0
            while n==0:
                tn = input('Wartosc N: ')
                try:
                    n = int(tn)
                except ValueError:
                    print('blad')
            print('Wynik: ' + rail.rail(t1, n))
        if menu == 6:
            t1 = input('Tekst do odszyfrowania: ').replace(' ', '_')
            n = 0
            while n == 0:
                tn = input('Wartosc N: ')
                try:
                    n = int(tn)
                except ValueError:
                    print('blad')
            print('Wynik: ' + derail.derail(t1, n))
        if menu == 7:
            t1 = input('Tekst do zaszyfrowania: ')
            k0 = int(input('Klucz1: '))
            k1 = int(input('Klucz2: '))
            out = encesar.encrypt_cesar(t1, k0, k1)
            print('Wynik: ' + out)
        if menu == 8:
            t1 = input('Tekst do odszyfrowania: ')
            k0 = int(input('Klucz1: '))
            k1 = int(input('Klucz2: '))
            out = decesar.decrypt_cesar(t1, k0, k1)
            print('Wynik: ' + out)
        if menu == 9:
            t1 = input('Tekst do zaszyfrowania: ')
            k0 = input('Klucz: ')
            out = envig.encrypt_vig(t1, k0)
            print('Wynik: ' + out)
        if menu == 10:
            t1 = input('Tekst do odszyfrowania: ')
            k0 = input('Klucz1: ')
            out = devig.decrypt_vig(t1, k0)
            print('Wynik: ' + out)


if __name__ == '__main__':
    main()
