"""
Wymagania:
Napisz program, który wczytuje od użytkownika wartości
i dodaje je do listy dopóki użytkownik nie poda wartości 'nie'

Wypisz listę na ekran.
"""

lista = []

while True:
    user_input = input("Podaj wartość: ")

    if user_input == "nie":
        break

    lista.append((user_input))

    print(lista)

