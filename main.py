from rail import rail, derail


if __name__ == '__main__':
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
        temp = input('> ')
        try:
            menu = int(temp)
        except ValueError:
            print('blad!')
        except KeyboardInterrupt:
            print('wyjscie')
            break
        if menu == 7:
