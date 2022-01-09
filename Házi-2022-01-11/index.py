# 5db  2 150 Ft -->


amount = int(input("Add meg a vásárolandó pólók darabszámát > "))
price = 500
counter = 0
result = 0

for i in range(amount):
    if price == 400:
        result += 400
    else:
        result += price
        counter += 1
        price -= 50
    print(result)
# print(result)
