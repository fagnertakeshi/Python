n1=input()
value1=[int(item) for item in input().split()]
n2=input()
value2=[int(item) for item in input().split()]
s1=set(value1)

print(len(s1.difference(value2)))
