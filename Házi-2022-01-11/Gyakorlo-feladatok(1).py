# ----importok----
import math
# ----------------

# 1. feladat > Helló világ: Készíts programot, mely kiírja a képernyőre azt a szöveget, hogy „Hello World”!
# print("Hello World!")


# 2. feladat >  Készíts programot, amely bekéri a felhasználó nevét, majd üdvözli őt a nevén szólítva!
name = input("Add meg a neved> ")
print("Üdvözöllek,", name)


# 3. feladat > Készíts programot, mely bekéri a felhasználótól, hogy a kasszában hány 100, 200 és 500 Ft-os található. A program számolja ki, hogy mennyi a beírt pénz összege!
szazasok = int(input("Add meg a Százasok számoát> "))
ketszazasok = int(input("Add meg a Kétszázasok számoát> "))
otszazasok = int(input("Add meg a Ötszázasok számoát> "))

ertek100 = szazasok * 100
ertek200 = ketszazasok * 200
ertek500 = otszazasok * 500

result = ertek100 + ertek200 + ertek500
print(result)


# 4 feladat > Készíts programot, amely bekér a felhasználótól egy valós számot (Celsius fok), az eredményt átváltja Fahrenheit értékbe, és kiírja az eredményt a képernyőre (0°C=32°F, 40°C=104°F, lineáris)! Írd meg ugyanezt fordítva is!
celsius = int(input("Add meg a celsius fokot> "))
if celsius == 0:
    print(32)
else:
    print((celsius * 1.8) + 3)

# 5 feladat >  Készíts programot, mely két időpontot kérdez a felhasználótól (óra, perc, másodperc külön), majd kiszámítja a két időpont közötti időtartamot ásodpercben, és az eredményt kiírja a képernyőre.
# -----------Eggyik óra-----------------------
ora1 = int(input("Hány óra?> "))
perc1 = int(input("Hány perc?> "))
masodperc1 = int(input("Hány másodperc?> "))

OraInSec1 = (ora1 * 60) * 60 #hunglish :D
MinInSec1 = perc1 * 60

result1 = OraInSec1 + MinInSec1 + masodperc1
# ---------------------------------------------

# ---------Másik óra---------------------------
ora2 = int(input("Hány óra?> "))
perc2 = int(input("Hány perc?> "))
masodperc2 = int(input("Hány másodperc?> "))

OraInSec2 = (ora2 * 60) * 60
MinInSec2 = perc2 * 60

result2 = OraInSec2 + MinInSec2 + masodperc2
# ---------------------------------------------

if result1 > result2:
    print(result1 - result2)
else:
    print(result2 - result1)


# 6 feladat >  Készíts programot, mely a felhasználótól bekért számról megállapítja, ogy az a.) pozitív, negatív vagy nulla, b.) egész vagy nem egész. Az eredményt a képernyőre szöveges válasz formájában írja ki!

num = float(input("Adj meg egy számot >"))

if num > 0:
    print("Pozitív")
elif num == 0:
    print("Ez nulla")
else:
    print("Negatív")


if num % 1 == 0:
    print("Egész!")
else:
    print("Nem egész!")

# 7 feladat > Készíts programot, mely beolvas a felhasználótól egy fizetést, és a fizetés nagyságától függően kiírja, hogy az alacsony, átlagos, vagy magas! A kategóriákat a saját preferenciád alapján határozhatod meg! :D

fizetes = int(input("Add meg a fizetésed> "))

if fizetes <= 185000:
    print("Kevés")
elif fizetes > 185000 >= 270000:
    print("átlagos")
elif fizetes > 270000:
    print("Magas")

# 8 feladat  > Egy turkálóban minden póló darabja 500 Ft. Ha egy vásárlás során valaki több darabot is vesz, a második ára már csak 450 Ft, a harmadik pedig 400 Ft, de a negyedik és további darabok is ennyibe kerülnek, tehát az ár a harmadik vásárlása után már nem csökken tovább. Írj programot, amely a vásárolt pólók darabszámának ismeretében megmondja, hogy mennyit fizet a vásárló!

amount = int(input("Add meg a vásárolandó pólók darabszámát > "))
price = 500
result = 0

for i in range(amount):
    if price == 400:
        result += 400
    else:
        result += price
        price -= 50
    print(result)

# 9 feladat >Számok kiírása: Az ábrán egy program algoritmusa látható, amely kiírja a számokat 1-től 20-ig.

# Gondolok egy számra, legyen ez 1.
# Ismétlés, amíg a szám ≤ 20
#     Leírom a számot.
#     Új sort kezdek.
#     Növelem a számot 1-gyel.
# Ismétlés eddig

gondoltSzam = 1
x = gondoltSzam

while x <= 20:
    print(x)
    x += 1

# 10 feladat >Írj programot, amely hatványozni képes! Kérdezze meg az alapot (valós) és a kitevőt (egész), és írja képernyőre a hatvány értékét!

alap = int(input("Add meg az alapot > "))
kitevo = int(input("Add meg az kitevőt > "))

result = alap ** kitevo
print(result)

# 11 feladat > Készíts programot, amely egy pozitív egész számról négyzetgyökvonás nélkül eldönti, hogy négyzetszám-e!

num = int(input("Adj meg egy pozitív egész számot > "))

i = num ** 0.5

if i**2 == num:
    print("Ez a szám négyzetszám!")
else:
    print("Ez a szám nem négyzetszám!")

# 12 feladat >Egy program bekér a felhasználótól két pozitív egész számot, és kiírja a két szám közötti összes páratlan számot. A program akkor is helyesen működik, ha a felhasználó előbb a felső, aztán az alsó határt adja meg (és fordítva is).  A program alogirtmusa a következő:
# -----------------------------------------------------------
# Első és második szám bekérése
# Ha első > második
#     alsó = második, felső = első
# Egyébként
#     alsó = első, felső = második
# A ciklusváltozó legyen alsó
# Amíg a ciklusváltozó kisebb vagy egyenlő a felsővel
#     Ha a ciklusváltozó páratlan
#        Írd ki a ciklusváltozót
#     Növeld a ciklusváltozót eggyel
# -----------------------------------------------------------
num1 = int(input("Adj meg egy pozitív egész számot > "))
num2 = int(input("Adj meg egy mésik pozitív egész számot > "))
if num1 > num2:
    lower = num2
    upper = num1
else:
    lower = num1
    upper = num2



helper = lower
while helper <= upper:
    if helper % 2 != 0:
        print(helper)
    helper += 1
