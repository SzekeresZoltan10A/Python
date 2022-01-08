# Készít egy üres listát, aminek a neve beatles legyen
beatles = []

# Használd az append() metódust a következő tagok hozzáadását reprezentálja: John Lennon, Paul McCartney, and George Harrison;
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("""
""")

print(beatles)

#használj for ciklust és append metódust egyszerre, és írasd ki a felhasználónak, hogy melyik folyamatnál vagy és milyen új nevet adsz majd a listához: Stu Sutcliffe, and Pete Best;
for i in range(1):
    print("Hozzáadom Stu Sutcliffe-t")
    beatles.append("Stu Sutcliffe")
    print("Hozzáadom Pete Best-et")
    beatles.append("Pete Best")

print(beatles)

# Töröld az előbbi két nevet a lista tartalmából
print("Törlöm az előző 2-őt")
del beatles[-1]
del beatles[-1]
print(beatles)

# Használd az insert() metódust hogy  Ringo Starr a lista legelejére kerüljön!
beatles.insert(0, "Ringo Starr")

#----------------------------------------------------------------------------------

print("""
""")
print("A végleges lista pedig>", beatles)
