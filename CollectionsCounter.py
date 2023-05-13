from collections import Counter

numberofShoes=int(input())

ListofShoes= [int(item) for item in input().split()]

listofshoes=Counter(ListofShoes)

numberofCustomers=int(input())


values = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        values.append(tuple(map(int, line.split())))
    except EOFError:
        break

total = 0
for buy in values:
    size, price = buy
    if size in listofshoes and listofshoes[size] > 0:
        total += price
        listofshoes[size] -= 1

print(total)