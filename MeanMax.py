import numpy

m,n=(int(x) for x in input().split())
arr=[]

for _ in range(m):
    arr.append([int(x) for x in input().split()])
       
print(numpy.max(numpy.min(arr,axis=1)))