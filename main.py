import random

"""
Zadanie 1

Napisz program, który pobierze od użytkownika liczby rozdzielone przecinkiem a następnie
policzy znajdzie ich max oraz min, bez używania wbudowanych funkcji.

"""

numbers = input("Wprowadź liczby rozdzielone przecinkiem: ")

numbers_list = numbers.split(",")
max_number = int(numbers_list[0])
min_number = int(numbers_list[0])

for number in numbers_list:
    if int(number) > max_number:
        max_number = int(number)
    if int(number) < min_number:
        min_number = int(number)

print("Największa liczba to:", max_number)
print("Najmniejsza liczba to:", min_number)

"""
Zadanie 2 

Napisz program, który wyświetli plan wycieczki – wybierając losowo z listy 10 największych
miast w Polsce miasta do odwiedzenia. Miast ma być 10, nie mogą się powtarzać.

"""

cities = ["Warszawa", "Kraków", "Łódź", "Wrocław", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Katowice"]
random.shuffle(cities)

print("Plan wycieczki:")
for i, city in enumerate(cities):
    print(f"{i+1}. {city}")

"""
Zadanie 3

3. Napisz grę – papier nożyce kamień. (60%)
  Gra pozwoli wybrać ilość rund.
  Pozwoli wybrać tryb gry – komputer / 2 graczy (hot seats)
  Pozwoli nazwać graczy.
  Zapamięta wynik z każdej rundy.
  Na koniec wyświetli listę wyników oraz ostateczny wynik z informacją, który gracz wygrał.
  W opcji hot seats należy użyć getpass:
 import getpass
 choice = getpass.getpass('wybór: ')
 print(choice)
"""