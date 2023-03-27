###     Mateusz Godlewski    ###

import math

"""
Zadanie 1

Napisz funkcję obliczającą i zwracającą ilość potrzebnych opakowań paneli w danym
pomieszczeniu, zakładając prostokątną podłogę i prostokątne panele. Dane wejściowe to długość i
szerokość podłogi. (do powierzchni pomieszczenia należy dodać 10%) długość i szerokość panela
oraz ilość paneli w opakowaniu. (10%)
"""


def panel_calc(dlugosc_podlogi, szerokosc_podlogi, dlugosc_panela, szerokosc_panela,
               ilosc_paneli_w_opakowaniu): return int(math.ceil(
    ((((dlugosc_podlogi * szerokosc_podlogi) * 1.1) / dlugosc_panela * szerokosc_panela) / ilosc_paneli_w_opakowaniu)))


print("Zadanie 1")
print("Potrzeba : " + str(panel_calc(4, 4, 0.20, 1, 10)))

"""
Zadanie 2

Napisz funkcję sprawdzającą czy podane liczby są liczbami pierwszymi w szybszy sposób niż w
przykładzie. Do funkcji można przekazać dowolną liczbę argumentów (liczby). Liczby 0 i 1 nie są
liczbami pierwszymi. (10%)
"""


def czy_pierwsza(n):
    for i in range(2, math.ceil(n / 2) + 1):
        if n % i == 0:
            return False
    return True


def prime(*tuple):
    for el in tuple:
        if (czy_pierwsza(el) and not el <= 2):
            print(el, " is prime")
        else:
            print(el, " is not prime")


print("Zadanie 2")
prime(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

"""
Zadanie 3

Napisz funkcję szyfrującą wiadomość szyfrem cezara. Dla ułatwienia należy przekształcić
wiadomość tak aby zawierała tylko wielkie lub małe litery.
Funkcja przyjmuje:
    wiadomość – tekst do zaszyfrowania,
    klucz – liczbę o ile należy przesunąć litery w alfabecie
    oraz zwraca zaszyfrowaną wiadomość w formie łańcucha znaków -string. (40%)
Funkcja szyfruje tylko litery – inne znaki wstawia do końcowej zaszyfrowanej wiadomości
    bez zmian(10%)
Funkcja rozwiązuje problem klucza przesuwającego litery poza zakres tablicy z alfabetem
    oraz problem podania klucza o dowolnej wielkości(20%).
Funkcja opcjonalnie przyjmuje dowolny alfabet. Domyślnie używa angielskiego(10%).
"""


def szyfruj(wiadomosc, klucz):
    wiadomosc = wiadomosc.lower()
    zaszyfrowanaWiadomosc = ""
    for znak in wiadomosc:
        if znak.isalpha():
            tmp = ((ord(znak)) + klucz) % 26 + 73
        else:
            tmp = ord(znak)
        zaszyfrowanaWiadomosc += chr(tmp)
    print(zaszyfrowanaWiadomosc)


print("Zadanie 3")
szyfruj("abz", 5)
