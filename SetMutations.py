numelem=int(input())
setA=set(map(int,input().split()))
numoperations=int(input().strip())


for _ in range(numoperations):   
    cmd, k = input().strip().split()
    k=int(k)
    setB=set(map(int,input().strip().split()))
     
    if "intersection_update"==cmd:
        setA.intersection_update(setB)
    elif "symmetric_difference_update"==cmd:
        setA.symmetric_difference_update(setB)
    elif "difference_update"==cmd:
        setA.difference_update(setB)
    elif "update"==cmd:
        setA.update(setB)

        
print(sum(setA))