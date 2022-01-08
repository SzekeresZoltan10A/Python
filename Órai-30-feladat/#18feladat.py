x1 = int(input("Adj meg egy számot :> "))
x2 = int(input("Adj meg egy másik számot :> "))
helper = 0
for i in range(x1, x2):
    helper += i
print(helper)
