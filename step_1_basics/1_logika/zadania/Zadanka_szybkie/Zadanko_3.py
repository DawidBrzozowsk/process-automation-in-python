"""
Pobierz od uzytkownika dane:
- imie
- nazwisko
- wiek

wyswietl powitanie uzględniajace powyzsze zmienne.
"""

def przywitanie():
    imie = input('Podaj swoje imie: ')
    nazwisko = input('Podaj swoje imie: ')
    wiek = input('Podaj swoje wiek: ')
    result = f'Witaj {imie} {nazwisko} w wieku {wiek}.'
    return result


print(przywitanie())
