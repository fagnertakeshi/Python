from itertools import product


A = map(int,input().split())
B = map(int,input().split())

tuples=product(A,B)

print(*tuple((int(x), int(y)) for (x, y) in tuples if ' ' not in (x,y)))