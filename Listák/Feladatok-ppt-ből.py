# 1-es feladat
beatles = []
print(beatles)

# 2-es feladat
# tagok hozzáadása
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)

# 3-as feladat
# passz

# 4-es feladat
# a 3-as feladatban lévőket kell törölni
del beatles[-1]
print(beatles)
del beatles[-1]
print(beatles)

# 5-ös feladat
beatles.insert(0, "Ringo Starr")
print(beatles)
