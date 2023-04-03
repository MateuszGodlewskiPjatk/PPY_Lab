###     Mateusz Godlewski    ###

"""
Zadanie 1

Wczyta z pliku dane dotyczące studentów – email, imię, nazwisko oraz liczbę uzyskanych
punktów z przedmiotu Podstawy Programowania Python. Dodatkowo w pliku mogą znajdować się
w tej samej linii dane dotyczące oceny końcowej oraz statusu (‘’, GRADED, MAILED).
Zakładamy, że plik istnieje – może być pusty lub zawiera podstawowe informacje:
email, imię, nazwisko, punkty. Do przechowywania danych w programie użyj słownika oraz
zagnieżdżania (20%)
"""


def wczytanie():
    students = {}
    file = open("students0.txt", "r")

    for line in file:
        students[line.strip().split(",")[0]] = line.strip().split(",")[1:]

    print(students)


# uruchomienie programu
print("| -------------------------------------|")
print("| Witaj w programie do wysylania maili |")
print("| -------------------------------------|")
print()
while True:
    print("Wybierz co mam zrobic wpisujac numer odpowiadajacy akcji:")
    print("1. Wczytaj dane z pliku")
    print("2. Dodaj studenta")
    print("3. Usun studenta")
    print("4. Wyslij maila do wszystkich studentow z wystawiona ocena")
    match input():
        case "1":
            wczytanie()
        case default:
            print("Wpisales znak spoza funkcjonalnych - program zakonczony - do zobaczenia w przyszlosci")
            break