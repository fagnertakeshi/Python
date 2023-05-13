import numpy

n, m, p = input().split(' ')
array_n = []
array_p = []

for _ in range(int(n)):
    array_n.append(list(map(int, input().split())))

for _ in range(int(m)):
    array_p.append(list(map(int, input().split())))

print(numpy.concatenate((array_n, array_p)  ) )