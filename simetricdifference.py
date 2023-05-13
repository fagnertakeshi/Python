n1=int(input())
a=set([int(item) for item in input().split(' ')])
n2=int(input())
b=set([int(item) for item in input().split(' ')])


diffa=a.difference(b)
diffb=b.difference(a)

for item in sorted(diffa.union(diffb)):
    print(item)