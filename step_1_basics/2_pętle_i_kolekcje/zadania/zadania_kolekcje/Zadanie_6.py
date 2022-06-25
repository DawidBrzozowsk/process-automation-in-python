"""
Stwórz listę trzech słowniki - Krystynę, Agnieszkę i Piotrka
Każdy kursant powinien mieć imię, informację o obecności i pracy domowej oraz punkty na egzaminie

Przejdź przez 6 dni kursu wypisując progres kursantów:
- Imię
- Obecność (ustaw losowo)
- Czy praca domowa jest odrobiona czy nie (ustaw losowo)
- Uzyskane punkty na egzaminie (ustaw losowo) (ustaw dopiero 6 dnia kursu)

Podpowiedź:
użyj random.choice do losowego ustawienia True i False
użyj random.randint do losowego ustawienia punktów (w zakresie 0 - 100)
"""
import copy
import random
from pprint import pprint

Krystyna = { 'Imię': 'Krystyna', 'Obecność': None, 'Praca domowa': None}
Agnieszka = { 'Imię': 'Agnieszka', 'Obecność': None, 'Praca domowa': None}
Piotrek = { 'Imię': 'Piotrek', 'Obecność': None, 'Praca domowa': None}

student_list = []

for day in range(1, 7):
    print(f'Dzień {day}')

    for student in [Krystyna, Agnieszka, Piotrek]:
        student_copy = copy.deepcopy(student)
        student_copy['Obecność'] = random.choice([True, False])
        student_copy['Praca domowa'] = random.choice([True, False])
        if day == 6:
            student_copy['Punkty na egzaminie'] = random.randint(0, 100)

        print(student_copy)
        student_list.append(student_copy)

pprint(student_list)