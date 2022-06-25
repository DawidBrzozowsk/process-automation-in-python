"""
Wymagania:
Napisz program, który wczytuje od użytkownika stringi w postaci klucz - wartość
Dodaj je do słownika.
Jeśli dany klucz istnieje w słowniku - nie rób nic.

Zapewnij możliwość podania kolejnych par klucz-wartość lub zaprzestawania ich podawania.

Wypisz elementy słownika na ekran w formie "klucz -> wartość"

Podpowiedź:
Użyj dwóch inputów do pobrania wartości
"""

slownik = {}

while True:
    user_input = input('Podaj klucz oraz wartość w formacie "klucz - wartość": ')

    if user_input == "exit":
        print("Wychodzenie z programu.")
        break

    if " - " not in user_input:
        print("Nieprawidłowy format, spróbuj jescze raz.")
        continue

    key, value = user_input.split(' - ')

    if key not in slownik.keys():
        slownik[key] = value

    for key_display, value_display in slownik.items():
        print(f'{key_display} -> {value_display}')