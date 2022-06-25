"""
Wymagania:
Sprawdź czy podana przez użytkownika liczba
jest podzielna przez 3, 5, 7

Wypisz wyniki na ekran.

Pamiętaj o komentarzach.

Rezultat wypisz na ekran.

Podpowiedź:
Odpowiednio formatuj stringi
"""


def zadanie_1(liczba):
    result = ''
    if liczba % 3 == 0:
        result += f'Liczba {liczba} jest podzielna przez 3.\n'
    else:
        result += f'Liczba {liczba} nie jest podzielna przez 3.\n'

    if liczba % 5 == 0:
        result += f'Liczba {liczba} jest podzielna przez 5.\n'
    else:
        result += f'Liczba {liczba} nie jest podzielna przez 5.\n'

    if liczba % 7 == 0:
        result += f'Liczba {liczba} jest podzielna przez 7.\n'
    else:
        result += f'Liczba {liczba} nie jest podzielna przez 7.\n'

    return result


user_input = int(input("Podaj liczbę: "))
print(zadanie_1(user_input))
