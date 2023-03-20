###     Mateusz Godlewski    ###
"""

Zadanie 1

"""

zmienna1 = "Python 2023"
zmienna2 = "Python 2023"
zmienna3 = "Python 2023"

print("Zadanie 1")
print("a)")
print(zmienna1==zmienna2==zmienna3)
print("b)")
print("zmienna 1: ", hex(id(zmienna1)), zmienna1)
print("zmienna 2: ", hex(id(zmienna2)), zmienna2)
print("zmienna 3: ", hex(id(zmienna3)), zmienna3)
zmienna3 = "Java 11"
print("zmienna 1: ", hex(id(zmienna1)), zmienna1)
print("zmienna 2: ", hex(id(zmienna2)), zmienna2)
print("zmienna 3: ", hex(id(zmienna3)), zmienna3)

"""

Zadanie 2

"""

pierwszaLiczba = input("Podaj pierwsza liczbe: ")
drugaLiczba = input("Podaj druga liczbe: ")
operator = input("Podaj operator: ")

if(operator == '+'):
    print(int(pierwszaLiczba) + int(drugaLiczba))
if(operator == '-'):
    print(int(pierwszaLiczba) - int(drugaLiczba))
if(operator == '*'):
    print(int(pierwszaLiczba) * int(drugaLiczba))
if(operator == '/'):
    print(int(pierwszaLiczba) / int(drugaLiczba))

"""

Zadanie 3

"""

pierszePytanie  = input("pytanie: 1.Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: ")
print("odpowiedź: ", pierszePytanie)
drugiePytanie   = input("pytanie: 2.W jakich okolicznościach czytasz książki najczęściej? ")
print("odpowiedź: ", drugiePytanie)
trzeciePytanie  = input("pytanie: 3.Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? ")
print("odpowiedź: ", trzeciePytanie)
czwartePytanie  = input("pytanie: 4.Po książki w jakiej formie sięgasz najczęściej? ")
print("odpowiedź: ", czwartePytanie)
piatePytanie    = input("pytanie: 5.Ile książek czytasz średnio w ciągu roku? ")
print("odpowiedź: ", piatePytanie)
szostePytanie   = input("pytanie: 6.Jak często średnio czytasz książki? ")
print("odpowiedź: ", szostePytanie)
siodmePytanie   = input("pytanie: 7.Po jakie gatunki książek sięgasz najczęściej? ")
print("odpowiedź: ", siodmePytanie)
imieNazwisko    = input("Jak się nazywasz? ")
print("odpowiedź: ", imieNazwisko.title())

