from rail import rail, derail
from cesar import encesar, decesar
import constants


def main():
    menu = 99
    while True:
        if menu == 99:
            print('Wybierz operacje do wykonania:\n'
                  '1. rail\n'
                  '2. derail\n'
                  '7. szyfrowanie cezara\n'
                  '8. deszyfrowanie cezara\n'
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
if __name__ == '__main__':
    main()