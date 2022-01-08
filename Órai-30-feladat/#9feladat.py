num = int(input("Adj meg egy pozitív egész számot :> "))
num2 = int(input("Adj meg egy másik pozitív egész számot :> "))

for i in range(num, num2):
    if i % 2 == 0:
        print(i)
