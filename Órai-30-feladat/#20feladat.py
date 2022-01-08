x1 = int(input("Adj meg egy pozitív egész számot:> "))
helper = 0

while helper != x1:
    print("-")
    helper += 1
    if helper != x1:
        print("-")
        helper += 1
    if helper != x1:
        print("+")
        helper += 1
