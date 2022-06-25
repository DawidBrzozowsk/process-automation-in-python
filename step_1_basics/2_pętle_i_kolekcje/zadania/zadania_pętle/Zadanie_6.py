"""
Wymagania:
Napisz program
pytajacy uzytkownika o litere a nastepnie
wypisujacy litery (z zakresu od a do z)
zaczynajac od a a konczac na wprowadzonej literze przez uzytkownika
zakoncz program jesli uzytkownik wpisze slowo "exit" lub "quit"
"""

from string import ascii_lowercase

while True:
    user_input = input("Podaj literę lub komendę: ")

    if user_input == 'exit' or user_input == 'quit':
        print('Wychodzenie z programu')
        break

    if len(user_input) > 1:
        print("Wprowadź tylko jedną literę lub komendy 'exit' lub 'quit' jeżeli chcesz wyjśc z programu.")
        continue

    if user_input not in ascii_lowercase:
        print('Nieznana litera, upewnij się że wprowadzasz mała literę.')
        continue

    for letter in ascii_lowercase:
        print(letter, end=' ')
        if user_input == letter:
            print('\n')
            break

