x = int(input("Add meg a dolgozat potszámát :>  "))

if x < 50:
    print("1 -es")
elif 50 <= x < 60:
    print("2 -es")
elif 60 <= x < 70:
    print("3 -as")
elif 70 <= x < 85:
    print("4 -es")
elif x > 80:
    print("5 -ös")
