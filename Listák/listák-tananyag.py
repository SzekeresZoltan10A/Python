# alap lista formája
numbers = [10, 5, 7, 2, 1]
print("Ez az eredeti lista", numbers)

# ---------------------------------------------------------------------------------------------

# sorrend a listákban
newList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
###################################
# 1 ==> 0.-ik tag,
# 2 ==> az 1. tag
# és így tovább
# ez minden listában így van
###################################

# ---------------------------------------------------------------------------------------------

# addjunk a mostani listánkhoz egy újabb elemet
numbers = [1, 2, 3, 4, 5, 6]
print("Ez az eredeti listánk:", numbers)
numbers[0] = 111
print("Ez a változtatott listánk:", numbers)

###################################
# numbers[y] = x
# az x egy új lista tag ami lehet szám vagy szó is
# az x-et beszúrja a lista y-onodik helyére
###################################

# ---------------------------------------------------------------------------------------------

# Fűzzük a 6-os számot a lista VÉGÉRE
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

###################################
# name.append(x)
# name ==> a listád neve
# x ==> a tag amit hozzá akarsz adni (ha stringet akarsz hozzádani akkor "" - ba kell tenni)
# hozáfűzi a megadott karaktert a lista VÉGÉRE [<== FONTOS HOGY A VÉGÉRE TESZI]
###################################

# ---------------------------------------------------------------------------------------------
print("insert")


# Fűzzük a 6-os számot a lista VÉGÉRE
numbers = [1, 2, 3, 4, 5]
numbers.insert(0, "új elem")
print(numbers)

###################################
# name.insert(x, y)
# name ==> a listád neve
# x ==> az a szám ami megadja, hogy melyi helyre kerüljön az új elem   !Figyenj a sorrendre!
# y ==> a tag amit hozzá akarsz adni (ha stringet akarsz hozzádani akkor "" - ba kell tenni)
# hozáfűzi a megadott karaktert a lista ELEJÉRE [<== FONTOS HOGY A ELEJÉRE TESZI]
###################################

# ---------------------------------------------------------------------------------------------

# Írassuk ki a programunkal a listának a hosszát
myList = [1, 2, "ListaElem", 20, 2.2]
print("A lista", len(myList), "tag hosszú.")

###################################
# len(x) függvény
# x ==> a lista neve
# megszámlálja a lista hosszát
###################################

# ---------------------------------------------------------------------------------------------

# Töröljünk egy elemet a listánkból

numbers = [1, 2, 3, 4, 5]
print("Az eredeti listánk:", numbers)
del numbers[1]
print("A módosított listánk:", numbers)

######################################################################
# del name[x]
# name ==> "a listád neve"
# # ==> és, "hogy hányadik tagot akarod kitörölni"
# !Figyelj a sorrendre, 0-val kezdődik a számolás!
######################################################################

# ---------------------------------------------------------------------------------------------
