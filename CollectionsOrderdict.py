from collections import OrderedDict
n=int(input())
products=OrderedDict()
order=[]
for _ in range(n):
    s=input()
    name = s[:s.rfind(' ')].strip()  # extract the product name
    price = int(s[s.rfind(' ')+1:])  # extract the price as a float
    if name in products:
        products[name] += price  # add the price to the existing product value
    else:
        products[name] = price
        order.append(name) 