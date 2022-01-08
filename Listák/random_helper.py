# kell a matek könyvtár a kerekítéshez
import math

# bekérjük a számot
myNum = int(input("Add meg a beszurandó számot :> "))

# a megadott listánk
hat_list = [1, 2, 3, 4, 5]

# a lista hossza
listLenght = len(hat_list)

# a lista hosszát elosztja 2-vel, majd felfelé* kerekíti, hogy megkapja a pontos közepét
# * azért felfelé mert ha egy páratlan számot elosztunk 2-vel akkot x.5 lesz és azt felfelé kerekítjük
result_float = listLenght / 2
result = math.ceil(result_float)

# hozzáadjuk a belért szöveget a közepére
hat_list.insert(result, myNum)
print(hat_list)

# kitöröljük a hozzáadott számot
del hat_list[result]
print(hat_list)
print(len(hat_list))
