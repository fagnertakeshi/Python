n1=int(input())
arr = set(map(int, input().split()))
n2=int(input())
for _ in range(n2):
    values=input().split()
    op=values[0]
 
    
    if len(values)==2:
        n3=int(values[1])
    if op == "pop":
        arr.pop()
    if op == "remove":
        if n3 in arr:
            arr.remove(n3)
    elif op == "discard":
        arr.discard(n3)
    
print(sum(arr))
