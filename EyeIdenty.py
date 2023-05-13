import numpy
value=[int(item) for item in input().split(' ')]
n=value[0]
m=value[1]
numpy.set_printoptions(legacy='1.13')
print(numpy.eye(n,m))