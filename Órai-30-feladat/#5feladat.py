a = int(input("Add meg az első számot:> "))
b = int(input("Add meg a második számot:> "))
c = int(input("Add meg a harmadik számot:> "))

if a + b == c:
    print("a + b = c")
elif a + c == b:
    print("a + c = b")
elif b + c == a:
    print("b + c = a")
